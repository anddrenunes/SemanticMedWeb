#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randint, randrange, choice
from time import strftime

import names
import addresses


yyyy = randint(1990,2012)
mm = randint(1,12)
dd = randint(1,28)
hh = randint(0,23)
mn = randint(0,59)
ss = randint(0,59)
ts = strftime("%Y-%m-%dT%H:%M:%SZ",(yyyy,mm,dd,hh,mn,ss,0,0,0))

def makeDemog(pat_id):

    gender = choice(('male','female'))
    gender = gender.capitalize()
    name = names.randName(gender)
    email = name[2]
    street = addresses.makeStreet()
    city = addresses.makeCity()
    phone = addresses.makePhone()

    ssn = str(randint(100,999)) + '-' + str(randint(10,99)) +'-'+str(randint(1000,9999))

    dlnum = name[1][0] + '-'+str(randint(100,999))+ '-'+str(randint(1000,9999))+ '-'+str(randint(100,999))+'-'+city[1]

    demog_str = """<?xml version="1.0" encoding="UTF-8"?>
<mlhim2:ccd-ca92a9c1-275f-42ca-b1a0-ac0a20cb2ec9 xmlns:mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1"
    xmlns:data-view="http://www.w3.org/2003/g/data-view#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.mlhim.org/xmlns/mlhim2/2_4_1 http://www.hkcr.net/ccd/ccd-ca92a9c1-275f-42ca-b1a0-ac0a20cb2ec9.xsd">
    <mlhim2:el-249daa52-7cdc-44bb-8cd8-7071993de08b>
        <mlhim2:cluster-subject>Demographics Cluster</mlhim2:cluster-subject>
        <mlhim2:el-a2bc25db-3111-4cd5-9825-d9c448cdd1a5>
            <mlhim2:el-7562af32-6e33-4a21-ab84-e9067331c465>
                <mlhim2:el-c3ba50ac-0370-4755-a138-94bba17691f9>
                    <mlhim2:data-name>Last Name</mlhim2:data-name>
                    <mlhim2:DvString-dv>"""+name[1]+"""</mlhim2:DvString-dv>
                </mlhim2:el-c3ba50ac-0370-4755-a138-94bba17691f9>
            </mlhim2:el-7562af32-6e33-4a21-ab84-e9067331c465>
            <mlhim2:el-a35f0879-4338-4908-a36f-ce16fc67cf7a>
                <mlhim2:el-0dc49ca0-94d7-46c9-b7a1-6c2b3b167f16>
                    <mlhim2:data-name>First Name</mlhim2:data-name>
                    <mlhim2:DvString-dv>"""+name[0]+"""</mlhim2:DvString-dv>
                </mlhim2:el-0dc49ca0-94d7-46c9-b7a1-6c2b3b167f16>
            </mlhim2:el-a35f0879-4338-4908-a36f-ce16fc67cf7a>
            <mlhim2:el-b291c9b2-f0ec-4ec2-9bed-5fac28afbd32>
                <mlhim2:el-1707ec28-169a-43da-92bf-83eef071255f>
                    <mlhim2:data-name>Email Address</mlhim2:data-name>
                    <mlhim2:valid-time-begin>"""+ts+"""</mlhim2:valid-time-begin>
                    <mlhim2:DvString-dv>"""+email+"""</mlhim2:DvString-dv>
                </mlhim2:el-1707ec28-169a-43da-92bf-83eef071255f>
            </mlhim2:el-b291c9b2-f0ec-4ec2-9bed-5fac28afbd32>
            <mlhim2:el-018c1d4e-d8e5-4537-b564-45191d5577bd>
                <mlhim2:el-8f2cc797-5603-46c2-a561-feb4a0bb7dd0>
                    <mlhim2:data-name>US Phone Number</mlhim2:data-name>
                    <mlhim2:DvString-dv>"""+phone+"""</mlhim2:DvString-dv>
                </mlhim2:el-8f2cc797-5603-46c2-a561-feb4a0bb7dd0>
            </mlhim2:el-018c1d4e-d8e5-4537-b564-45191d5577bd>
            <mlhim2:el-88d991a4-aa08-4767-aaab-fbf4197d5bd7>
                <mlhim2:el-c9fc43a3-ca79-491e-a788-963562ee3828>
                    <mlhim2:data-name>US SSN</mlhim2:data-name>
                    <mlhim2:DvString-dv>"""+ssn+"""</mlhim2:DvString-dv>
                </mlhim2:el-c9fc43a3-ca79-491e-a788-963562ee3828>
            </mlhim2:el-88d991a4-aa08-4767-aaab-fbf4197d5bd7>
            <mlhim2:el-09952004-eed1-4ba7-be91-340bc24af7c3>
                <mlhim2:el-1af72a9d-c5dd-4996-b3d9-adbad9c69e55>
                    <mlhim2:data-name>Drivers License Number</mlhim2:data-name>
                    <mlhim2:DvString-dv>"""+dlnum+"""</mlhim2:DvString-dv>
                </mlhim2:el-1af72a9d-c5dd-4996-b3d9-adbad9c69e55>
            </mlhim2:el-09952004-eed1-4ba7-be91-340bc24af7c3>
            <mlhim2:el-0b9a525a-fdc8-40f3-abd8-a83a993d418c>
                <mlhim2:el-665cf74e-8a0e-4b08-a1e4-58e3e0faf2ec>
                    <mlhim2:data-name>City Name</mlhim2:data-name>
                    <mlhim2:DvString-dv>"""+city[0]+"""</mlhim2:DvString-dv>
                </mlhim2:el-665cf74e-8a0e-4b08-a1e4-58e3e0faf2ec>
            </mlhim2:el-0b9a525a-fdc8-40f3-abd8-a83a993d418c>
            <mlhim2:el-ef538f44-e84b-455e-8db5-2ef40ef40b5e>
                <mlhim2:el-8e1b9ea1-56e4-4f25-90ae-f0d05a475766>
                    <mlhim2:data-name>State</mlhim2:data-name>
                    <mlhim2:DvString-dv>"""+city[1]+"""</mlhim2:DvString-dv>
                </mlhim2:el-8e1b9ea1-56e4-4f25-90ae-f0d05a475766>
            </mlhim2:el-ef538f44-e84b-455e-8db5-2ef40ef40b5e>
            <mlhim2:el-b380e079-af34-430d-88b4-599087fcdec4>
                <mlhim2:el-c2e6f182-ea59-491c-a2ec-04c8b6933f42>
                    <mlhim2:data-name>Zip Code</mlhim2:data-name>
                    <mlhim2:DvString-dv>"""+city[2]+"""</mlhim2:DvString-dv>
                </mlhim2:el-c2e6f182-ea59-491c-a2ec-04c8b6933f42>
            </mlhim2:el-b380e079-af34-430d-88b4-599087fcdec4>
            <mlhim2:el-06b0c425-f7ef-4d46-8573-97091ae52d60>
                <mlhim2:el-0ac3f22e-64ca-4309-be88-874cd14649a0>
                    <mlhim2:data-name>Gender</mlhim2:data-name>
                    <mlhim2:DvString-dv>"""+gender+"""</mlhim2:DvString-dv>
                </mlhim2:el-0ac3f22e-64ca-4309-be88-874cd14649a0>
            </mlhim2:el-06b0c425-f7ef-4d46-8573-97091ae52d60>
        </mlhim2:el-a2bc25db-3111-4cd5-9825-d9c448cdd1a5>
    </mlhim2:el-249daa52-7cdc-44bb-8cd8-7071993de08b>
</mlhim2:ccd-ca92a9c1-275f-42ca-b1a0-ac0a20cb2ec9>
"""

    return demog_str





