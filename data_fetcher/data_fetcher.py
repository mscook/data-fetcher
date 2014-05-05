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

import sys, argparse


def get_required_metadata():
    """
    """
    pass

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
    # Download the required metadata
    # Parse the metadata
    # Print some statistics
    # Download the fastq
    pass


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
