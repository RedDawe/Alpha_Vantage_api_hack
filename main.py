import csv
import time
from alpha_vantage.timeseries import TimeSeries
import os
import sys
import requests

print(requests.get('http://ip.42.pl/raw').text)

lst = []
with open('C:\companylist.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        #print(row[0])
        lst.append(row[0])

with open('C:\companylist (1).csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        #print(row[0])
        lst.append(row[0])

lst.pop(0)


ts0 = TimeSeries(key='', output_format='csv')
ts1 = TimeSeries(key='', output_format='csv')
ts2 = TimeSeries(key='', output_format='csv')

errs = []

def dw0(i):
    data, meta_data = ts0.get_daily(lst[i], outputsize='full')
    with open(str(i) + '.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for row in data:
            if row == ['    "Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."']:
                time.sleep(60)
                dw0(i)
            if row == ['    "Information": "Thank you for using Alpha Vantage! Please visit https://www.alphavantage.co/premium/ if you would like to have a higher API call volume."']:
                time.sleep(60)
                dw0(i)
            if row == ['    "Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY."']:
                errs.append(i)
            if (row != ['    "Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY."']) and (row != ['    "Information": "Thank you for using Alpha Vantage! Please visit https://www.alphavantage.co/premium/ if you would like to have a higher API call volume."'])  and (row != ['{']) and (row != ['}']) and (row != ['    "Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."']):
                spamwriter.writerow(row)

def dw1(i):
    data, meta_data = ts1.get_daily(lst[i+1], outputsize='full')
    with open(str(i+1) + '.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for row in data:
            if row == ['    "Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."']:
                time.sleep(60)
                dw1(i)
            if row == ['    "Information": "Thank you for using Alpha Vantage! Please visit https://www.alphavantage.co/premium/ if you would like to have a higher API call volume."']:
                time.sleep(60)
                dw1(i)
            if row == ['    "Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY."']:
                errs.append(i+1)
            if (row != ['    "Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY."']) and (row != ['    "Information": "Thank you for using Alpha Vantage! Please visit https://www.alphavantage.co/premium/ if you would like to have a higher API call volume."'])  and (row != ['{']) and (row != ['}']) and (row != ['    "Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."']):
                spamwriter.writerow(row)

def dw2(i):
    data, meta_data = ts2.get_daily(lst[i+2], outputsize='full')
    with open(str(i+2) + '.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for row in data:
            if row == ['    "Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."']:
                time.sleep(60)
                dw2(i)
            if row == ['    "Information": "Thank you for using Alpha Vantage! Please visit https://www.alphavantage.co/premium/ if you would like to have a higher API call volume."']:
                time.sleep(60)
                dw2(i)
            if row == ['    "Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY."']:
                errs.append(i+2)
            if (row != ['    "Error Message": "Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY."']) and (row != ['    "Information": "Thank you for using Alpha Vantage! Please visit https://www.alphavantage.co/premium/ if you would like to have a higher API call volume."'])  and (row != ['{']) and (row != ['}']) and (row != ['    "Note": "Thank you for using Alpha Vantage! Our standard API call frequency is 5 calls per minute and 500 calls per day. Please visit https://www.alphavantage.co/premium/ if you would like to target a higher API call frequency."']):
                spamwriter.writerow(row)


for item in range(3621, len(lst) - 2, 3):
    dw0(item)
    dw1(item)
    dw2(item)

    for iterator in errs:
        if os.path.exists(str(iterator) + '.csv'):
            os.remove(str(iterator) + '.csv')

    errs = []

