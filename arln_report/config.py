import re
import arln_report.ncbi_utils
from arln_report.user_args import user_args

SAMPLE = user_args.get('sample')
CDC_WGS_ID = user_args.get('cdc_wgs_id')
DATE_OF_REPORT = user_args.get('date_of_report')
USER = user_args.get('user')
EMAIL = user_args.get('email')
RUN_ID = user_args.get('run_id')
SEQUENCING_DATE = user_args.get('sequencing_date')
SRR_ID = user_args.get('srr_id')
SRA_UPLOAD_DATE = user_args.get('sra_upload_date')
CLASSIFIER = user_args.get('classifier')
ORGANISM_ID = user_args.get('organism_id')
MLST_1 = user_args.get('mlst_1')
MLST_1_SCHEME = user_args.get('mlst_scheme_1')
MLST_2 = user_args.get('mlst_2')
MLST_2_SCHEME = user_args.get('mlst_scheme_2')
AR_GENES = user_args.get('ar_genes')
QC_OUTCOME = user_args.get('qc_outcome')

if CDC_WGS_ID is None:
    pattern = re.compile(r"([\d]{4})JQ-([\d]{5})")
    id_groups = re.match(pattern, SAMPLE)
    id_year, id_digits = id_groups
    CDC_WGS_ID = f"{id_year}-JQ-{id_digits}"

if (SRR_ID is None) or (SRA_UPLOAD_DATE is None):
    SRR_ID, SRA_UPLOAD_DATE = ncbi_utils.retrieve_sra_metadata(SAMPLE)