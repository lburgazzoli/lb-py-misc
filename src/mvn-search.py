#!/usr/bin/env python3
#
# Copyright 2014 lb.
#
# Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import requests
import os
import sys

murl = 'http://search.maven.org/solrsearch/select'
pars = {'rows': '20', 'wt': 'json', 'q': sys.argv[1]}
prxs = {}

if os.environ.get('http_proxy'):
    prxs['http'] = os.environ.get('http_proxy')
if os.environ.get('http_proxy'):
    prxs['https'] = os.environ.get('https_proxy')
    
r = requests.get(murl, params=pars, proxies=prxs)
for result in r.json()['response']['docs']:
    print("{}:{}:{}".format(result['g'], result['a'], result['latestVersion']))

