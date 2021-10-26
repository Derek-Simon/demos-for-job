#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Derek on 2021/10/26
"""
-------------------------------------------------
File Name : main 
Description : Extract bank and market cap data from the JSON file bank_market_cap.json,
                Transform the market cap currency using the exchange rate data,
                Load the transformed data into a seperated CSV
Author : derek
Email : derek_simon@outlook.com
-------------------------------------------------
Change Activity:
    2021/10/26: create
-------------------------------------------------
"""

__author__ = 'derek'


import glob
import pandas as pd
from datetime import datetime


def extract_data_from_json(jsonfile):
    dataframe = pd.read_json(jsonfile)
    return dataframe


def extract():
    # create an empty data frame to hold extracted data
    extracted_data = pd.DataFrame(columns=['Name', 'Market Cap (US$ Billion)'])

    # process json files
    for jsonfile in glob.glob("./*.json"):
        extracted_data = extracted_data.append(extract_data_from_json(jsonfile), ignore_index=True)

    # print first 5 rows
    #print(extracted_data.iloc[:5])

    return extracted_data


def transform(data, rate):
    # exchange from USD to GBP
    data['Market Cap (US$ Billion)'] = round(data['Market Cap (US$ Billion)']*rate, 3)

    # Rename Market Cap (US$ Billion) to Market Cap (GBP$ Billion)
    data.rename(columns={'Market Cap (US$ Billion)': 'Market Cap (GBP$ Billion)'}, inplace=True)

    # print first 5 rows
    #print(data.iloc[:5])

    return data


def load(transformed_data, output_file):
    # Create a function that takes a dataframe and load it to a csv named bank_market_cap_gbp.csv.
    # Make sure to set index to False.
    transformed_data.to_csv(output_file, index=False)


def extract_certain_value(name):
    # Load the file exchange_rates.csv as a dataframe and find the exchange rate for British pounds with the symbol GBP,
    # store it in the variable  exchange_rate
    data = pd.DataFrame(
        columns=['', 'Rates'])  # create an empty data frame to hold extracted data
    data = data.append(pd.read_csv('exchange_rates.csv', index_col=0))
    exchange_rate = data.loc[name, 'Rates']
    return exchange_rate


def log(message, timestamp_format='%Y-%h-%d-%H:%M:%S'):
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')


if __name__ == '__main__':
    log("ETL Job Started")
    exchange_rate = extract_certain_value('GBP')
    extracted_data = extract()
    transformed_data = transform(extracted_data, exchange_rate)
    load(transformed_data, 'bank_market_cap_gbp.csv')
    log("Extract phase Started")
