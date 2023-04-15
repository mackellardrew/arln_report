import re
from Bio import Entrez
from arln_report.config import EMAIL

Entrez.email = EMAIL

def retrieve_biosample_id(sample_name):
    biosample_handle = Entrez.esearch(
        db="biosample", term=sample_name, retmax="40"
        # db="biosample", term=f"{sample_name}[All Fields]", retmax="40"
    )
    # Assume you'll always get a response, and the top hit will be the right one
    # May need to reasses later
    biosample_record = Entrez.read(biosample_handle)
    biosample_id = biosample_record['IdList'][0]
    # return biosample_record
    return [biosample_id]

def retrieve_sra_id(biosample_id):
    link_handle = Entrez.elink(db='sra', id=biosample_id, dbfrom='biosample')
    link_record = Entrez.read(link_handle)
    # Again, the assumption it'll always work and have same structure may be 
    # unwarranted; add exception handling for graceful exit if problems later
    sra_id = link_record[0]['LinkSetDb'][0]['Link'][0]['Id']
    return [sra_id]

def retrieve_sra_accession(sra_id):
    sra_handle = Entrez.esummary(db='sra', id=sra_id)
    sra_record = next(Entrez.parse(sra_handle))
    runs_part = sra_record['Runs']
    exp_part = sra_record['ExpXml']
    pattern = re.compile(r'.*Run acc="([\w]+)".*')
    # And yet again, the following might not always return something
    sra_accession = re.search(pattern, runs_part).groups()[0]
    sra_upload_date = sra_record['UpdateDate']
    return [sra_accession, sra_upload_date]

def retrieve_sra_metadata(sample_name):
    var_dict = {'sample_name': sample_name}
    for func, point, input_, output_keys in zip(
        (retrieve_biosample_id, retrieve_sra_id, retrieve_sra_accession),
        ('BioSample primary ID', 'SRA primary ID', 'SRA accession'),
        ('sample_name', 'biosample_id', 'sra_id'),
        (['biosample_id'], ['sra_id'], ['sra_accession', 'sra_upload_date'])
    ):
        try:
            outputs = func(var_dict[input_])
            # print(outputs)
            for output, output_key in zip(outputs, output_keys):
                var_dict[output_key] = output
        except (IndexError, KeyError):
            failure_msg = [
                f"SRA Accession could not be retrieved ({point})",
                f"SRA Upload Date could not be retrieved ({point})"
            ]
            return failure_msg[0], failure_msg[1]
    return var_dict['sra_accession'], var_dict['sra_upload_date']