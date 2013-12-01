# -*- coding: utf-8 -*-
"""
Created on Sun Dec 01 21:45:26 2013

@author: lehi
"""
import urllib2
import zipfile
import StringIO
import json

re = urllib2.urlopen('http://pilvilinna.cert.fi/opendata/autoreporter/json.zip')
f = re.read()
f = StringIO.StringIO(f)
zfile = zipfile.ZipFile(f, 'r')

data_ca = dict()
data_cc = dict()

#zfile = zipfile.ZipFile('E:\json.zip', 'r')
for name in zfile.namelist():
    infile = zfile.open(name, 'r')
    j = json.load(infile)
    for day in  j['autoreporter']['opendata']:
        for incident in day['asn']:
            for pcs in incident['ipaddress']:
                for inc in pcs['incident']:
                    if inc['category']['main'] in data_ca:
                        data_ca[inc['category']['main']] += 1
                    else:
                        data_ca[inc['category']['main']] = 1

                    if pcs['cc'] not in data_cc:
                        data_cc[pcs['cc']] = dict()
                    if pcs['city'] in data_cc[pcs['cc']]:
                        data_cc[pcs['cc']][pcs['city']] += 1
                    else:
                        data_cc[pcs['cc']][pcs['city']] = 1
                                              
zfile.close()
for key, value in data_ca.iteritems():
    print key + " " + str(value) #+ "\n"

for cc, data in data_cc.iteritems():
    for city, value in data.iteritems():
        print cc + city + " " + str(value) #+ "\n"
    
    