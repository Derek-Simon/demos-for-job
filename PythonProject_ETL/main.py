#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Derek on 2021/10/26
"""
-------------------------------------------------
File Name : main 
Description : data collection - batch process
 - data was collected from multiple sources and combined to become a single source of information
Author : derek
Email : derek_simon@outlook.com
-------------------------------------------------
Change Activity:
    2021/10/26: create
-------------------------------------------------
"""

__author__ = 'derek'

import glob                         # this module helps in selecting files
import pandas as pd                 # this module helps in processing CSV files
import xml.etree.ElementTree as ET  # this module helps in processing XML files.
from datetime import datetime


logfile = "logfile.txt"            # all event logs will be stored in this file
targetfile = "transformed_data.csv"   # file where transformed data is stored


def extract_data(type, file):
    """
    :param type: csv, json, xml
    :param file: file of data source to be processed
    :return: None if type doesn't match
    """
    if 'csv' == type:
        return pd.read_csv(file)
    elif 'json' == type:
        return pd.read_json(file,lines=True)
    elif 'xml' == type:
        dataframe = pd.DataFrame(columns=["name", "height", "weight"])
        tree = ET.parse(file)
        root = tree.getroot()
        for person in root:
            name = person.find("name").text
            height = float(person.find("height").text)
            weight = float(person.find("weight").text)
            dataframe = dataframe.append({"name": name, "height": height, "weight": weight}, ignore_index=True)
        return dataframe
    return None


def extract():
    extracted_data = pd.DataFrame(
        columns=['name', 'height', 'weight'])  # create an empty data frame to hold extracted data

    # process all csv files
    for csvfile in glob.glob("./datasource/*.csv"):
        extracted_data = extracted_data.append(extract_data('csv', csvfile), ignore_index=True)

    # process all json files
    for jsonfile in glob.glob("./datasource/*.json"):
        extracted_data = extracted_data.append(extract_data('json', jsonfile), ignore_index=True)

    # process all xml files
    for xmlfile in glob.glob("./datasource/*.xml"):
        extracted_data = extracted_data.append(extract_data('xml', xmlfile), ignore_index=True)

    return extracted_data


def transform(data):
    # Convert height which is in inches to millimeter
    # Convert the datatype of the column into float
    # data.height = data.height.astype(float)
    # Convert inches to meters and round off to two decimals(one inch is 0.0254 meters)
    data['height'] = round(data.height * 0.0254, 2)

    # Convert weight which is in pounds to kilograms
    # Convert the datatype of the column into float
    # data.weight = data.weight.astype(float)
    # Convert pounds to kilograms and round off to two decimals(one pound is 0.45359237 kilograms)
    data['weight'] = round(data.weight * 0.45359237, 2)
    return data


def load(targetfile, transformed_data):
    transformed_data.to_csv(targetfile)


def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')


if __name__ == '__main__':
    log("Extract phase Started")
    extracted_data = extract()
    log("Extract phase Ended")

    log("Transform phase Started")
    transformed_data = transform(extracted_data)
    log("Transform phase Ended")

    log("Load phase Started")
    load(targetfile, transformed_data)
    log("Load phase Ended")
