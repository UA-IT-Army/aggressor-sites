#!/bin/env python

import argparse
import json
from time import sleep
import cloudscraper
from requests.exceptions import ConnectionError, ReadTimeout
import threading

parser = argparse.ArgumentParser(description='check sites')
parser.add_argument('sites', action='append',
                    help='files enumerating sites')
parser.add_argument('--timeout', type=int, default=30)

args = parser.parse_args()

scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'firefox',
        'platform': 'windows',
        'mobile': False
    },
    interpreter='js2py'
)

def check_site(site, timeout=30):
    retries=5
    ok=False
    reason="NA"
    while retries>0:
        try:
            res=scraper.get(site, timeout=timeout)
            print("{} {}".format(site,res.status_code))
            retries=0
            ok=True
        except ConnectionError as ce:
            # print("ERROR: {}".format(str(ce)))
            retries -= 1
            sleep(5)
        except ReadTimeout as toe:
            # print(toe)
            retries = 0
            reason = "Timeout"
        except cloudscraper.exceptions.CloudflareChallengeError as cfce:
            retries = 0
            reason = "CloudFlareV2"
    if not ok:
        print("{} {}".format(site,reason))
    

threads=[]
for site_filename in args.sites:
    with open(site_filename, 'r') as site_file:
        data=json.loads(site_file.read())
        for k in data:
            thread=threading.Thread(target=check_site, name=k, args=(k,args.timeout))
            thread.start()
            threads.append(thread)

for thread in threads:
    thread.join()        