#!/usr/bin/env python3

import requests
import os
import sys

pars = {'rows': '20', 'wt': 'json', 'q': sys.argv[1]}
prxs = {}

if os.environ.get('http_proxy'):
    prxs['http'] = os.environ.get('http_proxy')
if os.environ.get('http_proxy'):
    prxs['https'] = os.environ.get('https_proxy')
    
r = requests.get("http://search.maven.org/solrsearch/select", params=pars, proxies=prxs)

for result in r.json()['response']['docs']:
    print("{}:{}:{}".format(result['g'], result['a'], result['latestVersion']))

