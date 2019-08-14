#!/usr/bin/env python

## Script for comparing city record holding ##

import os
import csv
import re


cropped_path = "/Volumes/lts2/CityRecord_Dinah/CityRecord/Cropped"
uncropped_path = "/Volumes/lts2/CityRecord_Dinah/CityRecord/Uncropped"

fieldnames = ["Cropped", "Uncropped"]

f = open("cityrecord_comp.csv", "w")
w = csv.DictWriter(f, fieldnames = fieldnames)

# for directory in os.scandir(cropped_path):
#     if directory.is_dir():
#         directory = directory.path
#         for subdir in os.scandir(directory):
#             if subdir.is_dir():
#                 subdir = os.path.basename(subdir)
#                 print(subdir)


## Setting up the regexes needed to find names ##
re_reel_num = re.compile("(R[0-9]{1,3})")
re_year = re.compile("(19[0-9]{2})")
re_month = re.compile("[0-9]_([A-Za-z]{3,9})_")
re_start_date = re.compile("([0-9]{1,2})-[0-9]{1,2}")
re_end_date = re.compile("[0-9]{1,2}-([0-9]{1,2})")
re_note = re.compile("[a-z]_([A-Za-z]+)_")



for directory in os.scandir(uncropped_path):
    if directory.is_dir():
        directory = directory.path
        for subdir in os.scandir(directory):
            if subdir.is_dir():
                subdir = os.path.basename(subdir)
                print(subdir)
                #
                # reel_num = re.findall(re_reel_num, subdir)[0]
                # year = re.findall(re_year, subdir)[0]
                #
                #
                # start_date = re.findall(re_start_date, subdir)
                # if len(start_date) == 0:
                #     print(directory + "\n" + subdir)
