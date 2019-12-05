#####################################################################################################
# Data ingestion script for the TBFY Knowledge Graph (https://theybuyforyou.eu/tbfy-knowledge-graph/)
# 
# This file contains a script that aggregates and prints out the statistics from the 'STATISTICS.TXT'
# file that are written in each release-date subfolder in the OpenOpps output folder when 
# running the openopps.py script.
# 
# Copyright: SINTEF 2017-2019
# Author   : Brian Elvesæter (brian.elvesater@sintef.no)
# License  : Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0)
# Project  : Developed as part of the TheyBuyForYou project (https://theybuyforyou.eu/)
# Funding  : TheyBuyForYou has received funding from the European Union's Horizon 2020
#            research and innovation programme under grant agreement No 780247
#####################################################################################################

#!/usr/bin/python

import config

import logging

import os
import sys
import getopt

import time
import datetime
from datetime import datetime
from datetime import timedelta


# **********
# Statistics
# **********

stats_releases = config.openopps_statistics.copy()

def print_stats():
    global stats_releases

    print("*********************************************************")
    for key in stats_releases.keys():
        print(str(key) + " = " + str(stats_releases[key]))
    print("*********************************************************")

def update_stats(file_stats):
    global stats_releases

    for key in stats_releases.keys():
        stats_releases[key] += int(file_stats[key])


# *************
# Main function
# *************
def main(argv):
    logging.basicConfig(level=config.logging["level"])

    start_date = ""
    end_date = ""
    openopps_folder = ""

    try:
        opts, args = getopt.getopt(argv, "hs:e:o:")
    except getopt.GetoptError:
        print("openopps_statistics.py -s <start_date> -e <end_date> -o <openopps_folder>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("openopps_statistics.py -s <start_date> -e <end_date> -o <openopps_folder>")
            sys.exit()
        elif opt in ("-s"):
            start_date = arg
        elif opt in ("-e"):
            end_date = arg
        elif opt in ("-o"):
            openopps_folder = arg

    logging.info("main(): start_date = " + start_date)
    logging.info("main(): end_date = " + end_date)
    logging.info("main(): openopps_folder = " + openopps_folder)

    start = datetime.strptime(start_date, "%Y-%m-%d")
    stop = datetime.strptime(end_date, "%Y-%m-%d")

    while start <= stop:
        release_date = datetime.strftime(start, "%Y-%m-%d")

        dirname = release_date
        stats_filepath = os.path.join(openopps_folder, dirname, 'STATISTICS.TXT')
        if os.path.isfile(stats_filepath):
            file_stats = {}
            with open(stats_filepath) as stats_file:
                for line in stats_file:
                    s_key, s_value = line.partition("=")[::2]
                    file_stats[s_key.strip()] = s_value
                update_stats(file_stats)

        start = start + timedelta(days=1)  # increase day one by one

    print_stats()


# *****************
# Run main function
# *****************
if __name__ == "__main__": main(sys.argv[1:])
