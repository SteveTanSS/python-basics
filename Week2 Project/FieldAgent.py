# 11/21/2021
# Author Steve Tan

import numpy as np
import pandas as pd
import logging
import datetime
import phonenumbers

from pandas.core.frame import DataFrame

# Set up the logger
logging.basicConfig(filename='NYLError.log', encoding='utf-8', level=logging.DEBUG)

#sort the file list based on the date with the earlier ones first
def sort_files(filelist):
    filelist.sort()
    return filelist

#check the number of indexes and return true if he files in ascending order have within 500 entries from the last
def check_file_counts(filelist):
    df = pd.read_csv(file_list[0])
    current_size = len(df.index)

    for x in filelist:
        df = pd.read_csv(x)
        df_size = len(df.index)
        if (abs(current_size - df_size) > 500):
            logging.err("Something is wrong with the file count sizes")
        current_size = df_size
    return True

def phone_valid(df:DataFrame):
    #todo validate phone

    print()

def state_valid():
    #todo validate state
    print()

def email_valid():
    #todo validate email
    print()

def update_df_headers(inputdf):
# returns a data frame with updated file headers
    clean_df = inputdf
    
    c1='Agent Writing Contract Start Date (Carrier appointment start date)'
    c2='Agent Writing Contract Start Date'
    c3='Agent Writing Contract Status (cancelled)'
    c4='Agent Writing Contract Status (active)'
    c5='Agent Writing Contract Status'

    if (c1 in clean_df):
        clean_df[c1].rename(c2)
    
    if (c3 in clean_df):
        clean_df[c3].rename(c5)

    if (c4 in clean_df):
        clean_df[c4].rename(c5)
    
    return clean_df


def file_processing(file_list):
    print()


#Program start

file_list = ["Python-Basics\\Week2 Project\\NYL_FieldAgent_20210205.csv", "Python-Basics\\Week2 Project\\NYL_FieldAgent_20210129.csv", "Python-Basics\\Week2 Project\\NYL_FieldAgent_20210212.csv", "Python-Basics\\Week2 Project\\NYL_FieldAgent_20210219.csv"]
sort_files(file_list)

try:
    check_file_counts(file_list)
except:
    print('Something is wrong with the file index sizes')
