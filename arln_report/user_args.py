import argparse
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument(
    "-w",
    "--waphl_sample_number",
    help=(
        "Main sample number used internally by WAPHL"
    ),
    type=str,
    dest="sample",
    required=True,
    default=os.getcwd(),
)
parser.add_argument(
    "-c",
    "--cdc_wgs_id",
    help=(
        "CDC WGS ID Number; should have form "
        "YYYY-JQ-#####, where '#####' is last 5 "
        "digits of waphl_sample_number"
    ),
    type=str,
    dest="cdc_wgs_id",
    default=None,
)
parser.add_argument(
    "-n",
    "--date_of_report",
    help="Date this report was generated",
    dest="date_of_report",
    default=datetime.strftime(datetime.now(), "%Y-%m-%d"),
)
parser.add_argument(
    "-u",
    "--user",
    help=(
        "Name of user generating this report"
    ),
    type=str,
    dest="user",
    default="undefined_arln_lab_member",
)
parser.add_argument(
    "-e",
    "--user_email",
    help=(
        "Email address of user preparing this report"
    ),
    type=str,
    dest="email",
    default="arlnlab@doh.wa.gov",
)
parser.add_argument(
    "-r",
    "--run_id",
    help=(
        "ID of sequencing run"
    ),
    type=str,
    dest="run_id",
    required=True,
    default=None,
)
parser.add_argument(
    "-d",
    "--sequencing_date",
    help=("Date of sequencing"),
    type=str,
    dest="sequencing_date",
    required=True,
    default=None,
)
parser.add_argument(
    "-i",
    "--srr_id",
    help=("SRA Accession ID"),
    type=str,
    dest="srr_id",
    default=None,
)
parser.add_argument(
    "-q",
    "--sra_upload_date",
    help=(
        "Date sample was uploaded to NCBI SRA server"
    ),
    type=str,
    dest="sra_upload_date",
    default=None,
)
parser.add_argument(
    "-c"
    "--classifier",
    help=("Taxonomic classifier used to generate organism ID"),
    type=str,
    dest="classifier",
    default="ANI_REFSEQ",
)
parser.add_argument(
    "-o"
    "--organism_id",
    help=(
        "Genus and Species name of sample"
    ),
    type=str,
    required=True,
    dest="organism_id",
)
parser.add_argument(
    "-m"
    "--mlst_1",
    help=(
        "MLST code 1"
    ),
    type=str,
    required=True,
    dest="mlst_1",
)
parser.add_argument(
    "-x"
    "--mlst_scheme_1",
    help=(
        "MLST scheme used for first MLST ID"
    ),
    type=str,
    required=True,
    dest="mlst_scheme_1",
)
parser.add_argument(
    "-n"
    "--mlst_2",
    help=(
        "MLST scheme used for secon[] MLST ID"
    ),
    type=str,
    dest="mlst_scheme_2",
)
parser.add_argument(
    "-y"
    "--mlst_scheme_2",
    help=(
        "MLST scheme used for second MLST ID"
    ),
    type=str,
    dest="mlst_scheme_2",
)
parser.add_argument(
    "-a"
    "--ar_genes",
    help=(
        "AR genes identified by WGS"
    ),
    type=str,
    dest="ar_genes",
)
parser.add_argument(
    "--amr_finder_genes",
    help=(
        "AR genes identified by AMRFinder"
    ),
    type=str,
    required=True,
    dest="amrf_genes",
)
parser.add_argument(
    "--beta_lactam_genes",
    help=(
        "Beta-Lactamase resistance genes identified by Phoenix"
    ),
    type=str,
    required=True,
    dest="beta_lactam_genes",
)
parser.add_argument(
    "-a"
    "--ar_genes",
    help=(
        "AR genes identified by WGS"
    ),
    type=str,
    required=True,
    dest="ar_genes",
)
parser.add_argument(
    "--qc_outcome",
    help=(
        "Automated QC cutoff from Phoenix"
    ),
    type=str,
    dest="qc_outcome",
)


user_args = vars(parser.parse_args())