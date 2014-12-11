#!/usr/bin/env python3

import requests
import os
import sys

params  = { 'rows': '20', 'wt': 'json', 'q': sys.argv[1]}
proxies = {}

if os.environ.get('http_proxy'):
    proxies['http']  = os.environ.get('http_proxy')
if os.environ.get('http_proxy'):
    proxies['https'] = os.environ.get('https_proxy')
    
r = requests.get("http://search.maven.org/solrsearch/select", 
    params  = params, 
    proxies = proxies
)

for result in r.json()['response']['docs']:
    print("{}:{}:{}".format(result['g'], result['a'], result['latestVersion']))

