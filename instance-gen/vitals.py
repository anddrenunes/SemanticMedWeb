#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import strftime
from random import randint, randrange, choice

temp_choice = randint(0,1)
yyyy = randint(1990,2012)
mm = randint(1,12)
dd = randint(1,28)
hh = randint(0,23)
mn = randint(0,59)
ss = randint(0,59)
ts = strftime("%Y-%m-%dT%H:%M:%SZ",(yyyy,mm,dd,hh,mn,ss,0,0,0))

def makeVitals():
    """Establish variables as strings using the limits from the CCD. Return a pre-formatted string for writing to the file."""


    vitals_str = """<?xml version="1.0" encoding="UTF-8"?>
    <mlhim2:ccd-949a53a0-0bc3-43ce-b900-1ff0b9c6798c xmlns:mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1"
        xmlns:data-view="http://www.w3.org/2003/g/data-view#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.mlhim.org/xmlns/mlhim2/2_4_1 http://www.hkcr.net/ccd/ccd-949a53a0-0bc3-43ce-b900-1ff0b9c6798c.xsd">
        <mlhim2:el-1ecee894-01a6-4736-bd95-6677bb70cb9e>
            <mlhim2:language>en-US</mlhim2:language>
            <mlhim2:encoding>utf-8</mlhim2:encoding>
            <mlhim2:el-9682f046-fc10-4822-9d20-670b85f667f6>
                <mlhim2:party-name>Self</mlhim2:party-name>
            </mlhim2:el-9682f046-fc10-4822-9d20-670b85f667f6>
            <mlhim2:el-2ef59764-f757-4f68-8b14-33fbab1cfedb>
                <mlhim2:cluster-subject>Care Cluster</mlhim2:cluster-subject>
                <mlhim2:el-a2bc25db-3111-4cd5-9825-d9c448cdd1a4>
                    <mlhim2:el-7562af32-6e33-4a21-ab84-e9067331c464>
                        <mlhim2:el-b470da9b-5eda-4fe8-a629-d324e248c733>
                            <mlhim2:data-name>Respiration</mlhim2:data-name>
                            <mlhim2:valid-time-begin>"""+ts+"""</mlhim2:valid-time-begin>
                            <mlhim2:magnitude>"""+str(randrange(5,180,1))+"""</mlhim2:magnitude>
                            <mlhim2:error>0</mlhim2:error>
                            <mlhim2:accuracy>0</mlhim2:accuracy>
                            <mlhim2:DvCount-units>Breathes Per Minute</mlhim2:DvCount-units>
                        </mlhim2:el-b470da9b-5eda-4fe8-a629-d324e248c733>
                    </mlhim2:el-7562af32-6e33-4a21-ab84-e9067331c464>
                    <mlhim2:el-228eff64-a79c-4baf-8271-01bd39c8cc8d>
                        <mlhim2:el-b1824a01-ffac-4a51-afff-a8a52dca9ca0>
                            <mlhim2:data-name>Temperature Device Type</mlhim2:data-name>
                            <mlhim2:DvString-dv>"""+choice(('Glass Bulb','Surface Tape','Infrared','Digital Probe'))+"""</mlhim2:DvString-dv>
                        </mlhim2:el-b1824a01-ffac-4a51-afff-a8a52dca9ca0>
                    </mlhim2:el-228eff64-a79c-4baf-8271-01bd39c8cc8d>
                    <mlhim2:el-0dd0fd4f-5d60-440a-8f0d-f92c19734b9b>
                        <mlhim2:el-779a5eeb-db86-414f-a7d7-7760e330ce0a>
                            <mlhim2:data-name>Temperature Location</mlhim2:data-name>
                            <mlhim2:DvString-dv>"""+choice(('Oral','Rectal','Forehead','Underarm, Right','Underarm, Left'))+"""</mlhim2:DvString-dv>
                        </mlhim2:el-779a5eeb-db86-414f-a7d7-7760e330ce0a>
                    </mlhim2:el-0dd0fd4f-5d60-440a-8f0d-f92c19734b9b>
                    <mlhim2:el-40c1535c-62f8-4fc7-8585-c34d5784160d>
                        <mlhim2:el-6d79fc4b-e640-4ffb-a9c4-a28a585bba66>
                            <mlhim2:data-name>Body Temperature</mlhim2:data-name>
                            <mlhim2:valid-time-begin>"""+ts+"""</mlhim2:valid-time-begin>
                            <mlhim2:magnitude>"""+str(randrange(0,110,1))+"""</mlhim2:magnitude>
                            <mlhim2:error>0</mlhim2:error>
                            <mlhim2:accuracy>0</mlhim2:accuracy>
                            <mlhim2:el-6c988591-e0fa-4e22-9dfc-fc83d28e9b69>
                                <mlhim2:data-name>Body Temperature</mlhim2:data-name>
                                <mlhim2:DvString-dv>"""+('C','F')[temp_choice]+"""</mlhim2:DvString-dv>
                                <mlhim2:terminology-abbrev>UCUM</mlhim2:terminology-abbrev>
                                <mlhim2:terminology-name>Unified Code for Units of Measure</mlhim2:terminology-name>
                                <mlhim2:terminology-version>1.8.2 Revision: 36299</mlhim2:terminology-version>
                                <mlhim2:terminology-code>"""+('CEL','DEGF')[temp_choice]+"""</mlhim2:terminology-code>
                            </mlhim2:el-6c988591-e0fa-4e22-9dfc-fc83d28e9b69>
                        </mlhim2:el-6d79fc4b-e640-4ffb-a9c4-a28a585bba66>
                    </mlhim2:el-40c1535c-62f8-4fc7-8585-c34d5784160d>
                    <mlhim2:el-72caeef6-1f12-41f9-a65c-3e8cc7f05f14>
                        <mlhim2:el-02555aa1-5e33-4dc3-9da6-e592839db930>
                            <mlhim2:data-name>Heart Rate (Pulse)</mlhim2:data-name>
                            <mlhim2:valid-time-begin>"""+ts+"""</mlhim2:valid-time-begin>
                            <mlhim2:magnitude>"""+str(randrange(30,250,1))+"""</mlhim2:magnitude>
                            <mlhim2:error>0</mlhim2:error>
                            <mlhim2:accuracy>0</mlhim2:accuracy>
                            <mlhim2:DvCount-units>Beats Per Minute</mlhim2:DvCount-units>
                        </mlhim2:el-02555aa1-5e33-4dc3-9da6-e592839db930>
                    </mlhim2:el-72caeef6-1f12-41f9-a65c-3e8cc7f05f14>
                    <mlhim2:el-63359d6f-116f-4170-bc8c-ab2687120430>
                        <mlhim2:el-186315c1-63f0-4880-a384-d850f159b36a>
                            <mlhim2:data-name>Patient Position</mlhim2:data-name>
                            <mlhim2:DvString-dv>"""+choice(('Sitting','Lying (Prone)','Standing'))+"""</mlhim2:DvString-dv>
                        </mlhim2:el-186315c1-63f0-4880-a384-d850f159b36a>
                    </mlhim2:el-63359d6f-116f-4170-bc8c-ab2687120430>
                    <mlhim2:el-bff07af1-0e13-43d0-8c06-ba9b2b83dd32>
                        <mlhim2:el-248f086e-f98c-432c-a38b-e8aa4710b4dc>
                            <mlhim2:data-name>Cuff Location</mlhim2:data-name>
                            <mlhim2:DvString-dv>"""+choice(('Upper Arm, Right','Upper Arm, Left','Wrist, Right','Wrist, Left'))+"""</mlhim2:DvString-dv>
                        </mlhim2:el-248f086e-f98c-432c-a38b-e8aa4710b4dc>
                    </mlhim2:el-bff07af1-0e13-43d0-8c06-ba9b2b83dd32>
                    <mlhim2:el-3404a9ff-c6e3-47a8-abd9-fd82c0400845>
                        <mlhim2:el-7ecfdbba-e863-4417-a41c-a09f035d2a2c>
                            <mlhim2:data-name>BP Device Type</mlhim2:data-name>
                            <mlhim2:DvString-dv>"""+choice(('Digital','Manual Analog','Automatic Analog'))+"""</mlhim2:DvString-dv>
                        </mlhim2:el-7ecfdbba-e863-4417-a41c-a09f035d2a2c>
                    </mlhim2:el-3404a9ff-c6e3-47a8-abd9-fd82c0400845>
                    <mlhim2:el-42a1409a-9e80-4b80-9781-2f04bee48538>
                        <mlhim2:el-3ad51caa-b762-42a8-a284-96707d37240b>
                            <mlhim2:data-name>Systolic Pressure</mlhim2:data-name>
                            <mlhim2:valid-time-begin>"""+ts+"""</mlhim2:valid-time-begin>
                            <mlhim2:magnitude>"""+str(randrange(40,240,1))+"""</mlhim2:magnitude>
                            <mlhim2:error>0</mlhim2:error>
                            <mlhim2:accuracy>0</mlhim2:accuracy>
                            <mlhim2:el-5420c69b-c26f-4aae-a133-5f1922351fb6>
                                <mlhim2:data-name>Systolic Pressure</mlhim2:data-name>
                                <mlhim2:DvString-dv>Observable Systolic Pressure</mlhim2:DvString-dv>
                                <mlhim2:terminology-abbrev>SNOMED-CT</mlhim2:terminology-abbrev>
                                <mlhim2:terminology-name>Systematized Nomenclature of Medicine Clinical Terms</mlhim2:terminology-name>
                                <mlhim2:terminology-version>07/2009</mlhim2:terminology-version>
                                <mlhim2:terminology-code>271649006</mlhim2:terminology-code>
                            </mlhim2:el-5420c69b-c26f-4aae-a133-5f1922351fb6>
                        </mlhim2:el-3ad51caa-b762-42a8-a284-96707d37240b>
                    </mlhim2:el-42a1409a-9e80-4b80-9781-2f04bee48538>
                    <mlhim2:el-ddd4569c-d689-47a9-bfdf-0659de76d239>
                        <mlhim2:el-9e091f86-fa5f-4f90-af2d-98046df1cd9c>
                            <mlhim2:data-name>Diastolic Pressure</mlhim2:data-name>
                            <mlhim2:valid-time-begin>"""+ts+"""</mlhim2:valid-time-begin>
                            <mlhim2:magnitude>"""+str(randrange(30,150,1))+"""</mlhim2:magnitude>
                            <mlhim2:error>0</mlhim2:error>
                            <mlhim2:accuracy>0</mlhim2:accuracy>
                            <mlhim2:el-77c990aa-2fdb-4025-9ef2-c624cd024751>
                                <mlhim2:data-name>Diastolic Pressure</mlhim2:data-name>
                                <mlhim2:DvString-dv>Observable Diastolic Pressure</mlhim2:DvString-dv>
                                <mlhim2:terminology-abbrev>SNOMED-CT</mlhim2:terminology-abbrev>
                                <mlhim2:terminology-name>Systematized Nomenclature of Medicine Clinical Terms</mlhim2:terminology-name>
                                <mlhim2:terminology-version>07/2009</mlhim2:terminology-version>
                                <mlhim2:terminology-code>271650006</mlhim2:terminology-code>
                            </mlhim2:el-77c990aa-2fdb-4025-9ef2-c624cd024751>
                        </mlhim2:el-9e091f86-fa5f-4f90-af2d-98046df1cd9c>
                    </mlhim2:el-ddd4569c-d689-47a9-bfdf-0659de76d239>
                </mlhim2:el-a2bc25db-3111-4cd5-9825-d9c448cdd1a4>
            </mlhim2:el-2ef59764-f757-4f68-8b14-33fbab1cfedb>
        </mlhim2:el-1ecee894-01a6-4736-bd95-6677bb70cb9e>
    </mlhim2:ccd-949a53a0-0bc3-43ce-b900-1ff0b9c6798c>"""

    return vitals_str
