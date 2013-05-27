#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os

import requests

#if you do not have a standard installation on the localhost you will need to edit this:
db_url = 'http://localhost:8080/exist/rest/db/'

try:
    user = sys.argv[1]
    pw = sys.argv[2]
except:
    print "You must enter a username and password on the commandline."
    exit()
    
auth = requests.auth.HTTPBasicAuth(user,pw)

header = {'content-type':'application/xml'}

rootDir = 'smw'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
        f = open(dirName+'/'+fname,'rb').read()
        r = requests.put(db_url+'apps/'+dirName+'/'+fname, data=f, auth=auth)
        print r.status_code

rootDir = 'data'
for dirName, subdirList, fileList in os.walk(rootDir):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)
        f = open(dirName+'/'+fname,'rb').read()
        r = requests.put(db_url+'apps/'+dirName+'/'+fname, data=f, auth=auth)
        print r.status_code


