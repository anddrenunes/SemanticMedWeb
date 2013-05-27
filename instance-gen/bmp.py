#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import strftime
from random import *
from decimal import *

def makeBMP():
    na = Decimal(uniform(130,150)).quantize(Decimal('.01'))
    g = Decimal(uniform(50,150)).quantize(Decimal('.01'))
    k = Decimal(uniform(3,6)).quantize(Decimal('.01'))
    bun = Decimal(uniform(5,22)).quantize(Decimal('.01'))
    c = Decimal(uniform(.5,1.5)).quantize(Decimal('.01'))

    yyyy = randint(1990,2012)
    mm = randint(1,12)
    dd = randint(1,28)
    hh = randint(0,23)
    mn = randint(0,59)
    ss = randint(0,59)
    ts = strftime("%Y-%m-%dT%H:%M:%SZ",(yyyy,mm,dd,hh,mn,ss,0,0,0))

    bmp_str = """<?xml version="1.0" encoding="UTF-8"?>
    <mlhim2:ccd-fa706c7a-f08a-4c80-8ce3-8ab7e2699517 xmlns:mlhim2="http://www.mlhim.org/xmlns/mlhim2/2_4_1"
        xmlns:data-view="http://www.w3.org/2003/g/data-view#" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.mlhim.org/xmlns/mlhim2/2_4_1 http://www.hkcr.net/ccd/ccd-fa706c7a-f08a-4c80-8ce3-8ab7e2699517.xsd">
        <mlhim2:el-ef7dc8ee-5cf5-47cc-92a5-7143094b88c8>
            <mlhim2:language>en-US</mlhim2:language>
            <mlhim2:encoding>utf-8</mlhim2:encoding>
            <mlhim2:el-c2c7e652-46f8-498a-99d0-c85005d98f6f>
                <mlhim2:party-name>Self</mlhim2:party-name>
            </mlhim2:el-c2c7e652-46f8-498a-99d0-c85005d98f6f>
            <mlhim2:el-a69717be-7b3f-4be7-9fec-80f8ec1891e8>
                <mlhim2:cluster-subject>Care Cluster</mlhim2:cluster-subject>
                <mlhim2:el-0c71fe4c-8dd2-4d0f-af05-15b5b7b9de24>
                    <mlhim2:el-57449ea7-a165-4bda-a16e-f654d36a7885>
                        <mlhim2:el-51b66f95-13b5-4e25-9c08-5e6d43aeba79>
                            <mlhim2:data-name>Creatinine</mlhim2:data-name>
                            <mlhim2:valid-time-begin>"""+ts+"""</mlhim2:valid-time-begin>
                            <mlhim2:magnitude>"""+str(c)+"""</mlhim2:magnitude>
                            <mlhim2:error>0</mlhim2:error>
                            <mlhim2:accuracy>0</mlhim2:accuracy>
                            <mlhim2:el-6aeb7189-79f8-4f2c-ab66-c46c6ab9f4de>
                                <mlhim2:data-name>Creatinine</mlhim2:data-name>
                                <mlhim2:DvString-dv>milligrams per deciliter</mlhim2:DvString-dv>
                                <mlhim2:terminology-abbrev>UCUM</mlhim2:terminology-abbrev>
                                <mlhim2:terminology-name>Unified Code for Units of Measure</mlhim2:terminology-name>
                                <mlhim2:terminology-version>1.8.2 Revision: 36299</mlhim2:terminology-version>
                                <mlhim2:terminology-code>mg/dL</mlhim2:terminology-code>
                            </mlhim2:el-6aeb7189-79f8-4f2c-ab66-c46c6ab9f4de>
                        </mlhim2:el-51b66f95-13b5-4e25-9c08-5e6d43aeba79>
                    </mlhim2:el-57449ea7-a165-4bda-a16e-f654d36a7885>
                    <mlhim2:el-ccc6596a-d918-4205-b8ac-8885892eac37>
                        <mlhim2:el-866aa21b-9cd2-48cc-9c18-8e799086d222>
                            <mlhim2:data-name>Urea (BUN)</mlhim2:data-name>
                            <mlhim2:valid-time-begin>"""+ts+"""</mlhim2:valid-time-begin>
                            <mlhim2:magnitude>"""+str(bun)+"""</mlhim2:magnitude>
                            <mlhim2:error>0</mlhim2:error>
                            <mlhim2:accuracy>0</mlhim2:accuracy>
                            <mlhim2:el-d6060f5c-f666-41a5-97c7-48f065bc7991>
                                <mlhim2:data-name>Urea (BUN)</mlhim2:data-name>
                                <mlhim2:DvString-dv>milligrams per deciliter</mlhim2:DvString-dv>
                                <mlhim2:terminology-abbrev>UCUM</mlhim2:terminology-abbrev>
                                <mlhim2:terminology-name>Unified Code for Units of Measure</mlhim2:terminology-name>
                                <mlhim2:terminology-version>1.8.2 Revision: 36299</mlhim2:terminology-version>
                                <mlhim2:terminology-code>mg/dL</mlhim2:terminology-code>
                            </mlhim2:el-d6060f5c-f666-41a5-97c7-48f065bc7991>
                        </mlhim2:el-866aa21b-9cd2-48cc-9c18-8e799086d222>
                    </mlhim2:el-ccc6596a-d918-4205-b8ac-8885892eac37>
                    <mlhim2:el-6245099f-9639-400e-a6a2-e6f305e2e0cd>
                        <mlhim2:el-781e9dda-055a-4a95-bee3-d482c44d1186>
                            <mlhim2:data-name>Potassium (K)</mlhim2:data-name>
                            <mlhim2:valid-time-begin>"""+ts+"""</mlhim2:valid-time-begin>
                            <mlhim2:magnitude>"""+str(k)+"""</mlhim2:magnitude>
                            <mlhim2:error>0</mlhim2:error>
                            <mlhim2:accuracy>0</mlhim2:accuracy>
                            <mlhim2:el-dc881c59-91f9-4dc0-ac64-f27b38294a70>
                                <mlhim2:data-name>Potassium (K)</mlhim2:data-name>
                                <mlhim2:DvString-dv>milliequivalent per liter</mlhim2:DvString-dv>
                                <mlhim2:terminology-abbrev>UCUM</mlhim2:terminology-abbrev>
                                <mlhim2:terminology-name>Unified Code for Units of Measure</mlhim2:terminology-name>
                                <mlhim2:terminology-version>1.8.2 Revision: 36299</mlhim2:terminology-version>
                                <mlhim2:terminology-code>meq/L</mlhim2:terminology-code>
                            </mlhim2:el-dc881c59-91f9-4dc0-ac64-f27b38294a70>
                        </mlhim2:el-781e9dda-055a-4a95-bee3-d482c44d1186>
                    </mlhim2:el-6245099f-9639-400e-a6a2-e6f305e2e0cd>
                    <mlhim2:el-4ca15845-9b70-44fb-bcba-a8fd22cb0a3a>
                        <mlhim2:el-28f7ec54-254b-4b66-9c42-3b275fc1df38>
                            <mlhim2:data-name>Glucose</mlhim2:data-name>
                            <mlhim2:magnitude>"""+str(g)+"""</mlhim2:magnitude>
                            <mlhim2:error>0</mlhim2:error>
                            <mlhim2:accuracy>0</mlhim2:accuracy>
                            <mlhim2:el-2cf3eb93-f83a-41cd-807a-da2b6d44c0e4>
                                <mlhim2:data-name>Glucose</mlhim2:data-name>
                                <mlhim2:DvString-dv>milligrams per deciliter</mlhim2:DvString-dv>
                                <mlhim2:terminology-abbrev>UCUM</mlhim2:terminology-abbrev>
                                <mlhim2:terminology-name>Unified Code for Units of Measure</mlhim2:terminology-name>
                                <mlhim2:terminology-version>1.8.2 Revision: 36299</mlhim2:terminology-version>
                                <mlhim2:terminology-code>mg/dL</mlhim2:terminology-code>
                            </mlhim2:el-2cf3eb93-f83a-41cd-807a-da2b6d44c0e4>
                        </mlhim2:el-28f7ec54-254b-4b66-9c42-3b275fc1df38>
                    </mlhim2:el-4ca15845-9b70-44fb-bcba-a8fd22cb0a3a>
                    <mlhim2:el-fd897186-1ec9-4534-bdca-3be434c93924>
                        <mlhim2:el-f6c5ea6e-6458-4799-874d-7f3d365d260d>
                            <mlhim2:data-name>Sodium (Na)</mlhim2:data-name>
                            <mlhim2:valid-time-begin>"""+ts+"""</mlhim2:valid-time-begin>
                            <mlhim2:magnitude>"""+str(na)+"""</mlhim2:magnitude>
                            <mlhim2:error>0</mlhim2:error>
                            <mlhim2:accuracy>0</mlhim2:accuracy>
                            <mlhim2:el-3f74aa98-9c88-4d37-851a-31f197aab453>
                                <mlhim2:data-name>Sodium (Na)</mlhim2:data-name>
                                <mlhim2:DvString-dv>milliequivalent per liter</mlhim2:DvString-dv>
                                <mlhim2:terminology-abbrev>UCUM</mlhim2:terminology-abbrev>
                                <mlhim2:terminology-name>Unified Code for Units of Measure</mlhim2:terminology-name>
                                <mlhim2:terminology-version>1.8.2 Revision: 36299</mlhim2:terminology-version>
                                <mlhim2:terminology-code>meq/L</mlhim2:terminology-code>
                            </mlhim2:el-3f74aa98-9c88-4d37-851a-31f197aab453>
                        </mlhim2:el-f6c5ea6e-6458-4799-874d-7f3d365d260d>
                    </mlhim2:el-fd897186-1ec9-4534-bdca-3be434c93924>
                </mlhim2:el-0c71fe4c-8dd2-4d0f-af05-15b5b7b9de24>
            </mlhim2:el-a69717be-7b3f-4be7-9fec-80f8ec1891e8>
        </mlhim2:el-ef7dc8ee-5cf5-47cc-92a5-7143094b88c8>
    </mlhim2:ccd-fa706c7a-f08a-4c80-8ce3-8ab7e2699517>"""

    return bmp_str
