#!/usr/bin/env python

# Copyright 2014 Beatson Laboratory Licensed under the
# Educational Community License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may
# obtain a copy of the License at
#
# http://www.osedu.org/licenses/ECL-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.

"""
A tool to programatically mass download data from the ENA 
"""

import sys, argparse, urllib2


def get_required_metadata(study_id):
    """
    Fetch a txt document containing useful data Given a valid SRA/ENA study id
    
    :param study_id: a valid SRA/ENA study id
    :type study_id: string
    
    :returns: the txt formatted metadata info as a string
    """
    BASE = ("http://www.ebi.ac.uk/ena/data/warehouse/filereport?accession="
            "CURRENT&result=read_run&fields=study_accession,"
            "secondary_study_accession,sample_accession,"
            "secondary_sample_accession,experiment_accession,run_accession"
            ",scientific_name,instrument_model,library_layout,fastq_ftp"
            ",fastq_galaxy,submitted_ftp,submitted_galaxy,col_tax_id,"
            "col_scientific_name,sra_ftp,sra_galaxy")
    BASE = BASE.replace('CURRENT', study_id)
    response = urllib2.urlopen(BASE)
    # Turn into a list
    return response.read().split('\n')

def parse_meta_data():
    """
    """
    pass


def print_data_stats():
    """
    """
    pass


def download_files():
    """
    """
    pass


def core(args):
    """
    The core function (accepts argparse and calls required)

    :param args: an argparse object
    """
    # Parse the metadata
    # Print some statistics
    # Download the fastq
    metadata_file = get_required_metadata(args.study_id)
    print metadata_file


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description=
                'Bulk downloader given SRA/ENA study accession',
                epilog='Written by the Beatson Lab. http://www.beatsonlab.com')
        parser.add_argument("study_id", help="A valid SRA/ENA accession")
        parser.set_defaults(func=core)
        args = parser.parse_args()
        args.func(args)
        sys.exit(0)
    except:
        pass
