#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Create data instances for CCDs and simulate a clinical record system.
Used for persistence testing, querying, etc.
Currently (2012-10-10) only creates data for three CCDs:
ccd-fa706c7a-f08a-4c80-8ce3-8ab7e2699517.xsd - Demographics
ccd-949a53a0-0bc3-43ce-b900-1ff0b9c6798c.xsd - Vital Signs
ccd-fa706c7a-f08a-4c80-8ce3-8ab7e2699517.xsd - Basic Metabolic Panel (BMP)


To be adapted later for creating data for a directory of CCDs.

See README.txt for complete instructions.

Copyright, 2012 - Timothy W. Cook & Contributors
License: GPL V.3 http://www.gpl.org
"""

import os
import sys
import time
import codecs
from datetime import datetime
from random import *
import uuid

import vitals
import bmp
import demog

curdir = os.getcwd()

#read from ccd2data.cfg file
f = open('instance-gen.cfg','r')
cfg = f.readlines()

numrecs = int(cfg[3].strip('records='))
mininstances = int(cfg[4].strip('mininstances='))
maxinstances = int(cfg[5].strip('maxinstances='))
f.close()


def ccdVitals(recid):
    cnt = randint(mininstances,maxinstances)
    v_id = 0
    for n in range(1,cnt):
        xmlfile = "vitals-" + (str(v_id).zfill(10))+'.xml'
        f = open(recid+'/'+xmlfile,'w')
        f.write(vitals.makeVitals())
        f.close()
        v_id+=1
    print "Created " + str(cnt) + " Vitals instances."

def ccdBMP(recid):
    cnt = randint(mininstances,maxinstances)
    b_id = 0
    for n in range(1,cnt):
        xmlfile = "bmp-" + (str(b_id).zfill(10))+'.xml'
        f = open(recid+'/'+xmlfile,'w')
        f.write(bmp.makeBMP())
        f.close()
        b_id +=1
    print "Created " + str(cnt) + " BMP instances.\n"

def ccdDemog(recid):
    """Write one demographics.xml per record."""
    pat_id = recid[10:]
    xmlfile = 'demographics.xml'
    f = open(recid+'/'+xmlfile,'w')
    f.write(demog.makeDemog(pat_id))
    f.close()

#Create MLHIM-EMR
os.mkdir(curdir+'/MLHIM-EMR')
print "Creating Records: "
# Create patient records as folders/directories
pr_id = 0

for x in range(1,numrecs+1):
    recid = 'MLHIM-EMR'+'/pr-'+(str(pr_id).zfill(10))
    print x, " of ", numrecs," Record Number: ",recid
    os.mkdir(curdir+'/'+recid)
    ccdVitals(recid)
    ccdBMP(recid)
    ccdDemog(recid)
    pr_id += 1

print "MLHIM EMR simulation data creation is complete."
print "For more information about MLHIM please join the MLHIM Community on Google Plus:"
print "gplus.to/MLHIMComm and Follow the MLHIM page: gplus.to/MLHIM"