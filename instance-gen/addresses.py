#!/usr/bin/python
# -*- coding: utf-8 -*-
# some data is from www.geonames.org

from random import *

streets = None

def makeStreet():
    f = open('allstreets.txt')
    streets = f.readlines()
    f.close()

    street_type = choice(('Alley', 'Arcade', 'Arch', 'Avenue', 'Bay', 'Boulevard', 'Bypass', 'Byway', 'Canyon', 'Causeway', 'Circle', 'Close', 'Court', 'Cove', 'Crescent', 'Croft', 'Dell', 'Drive', 'Expressway', 'Freeway', 'Gardens', 'Garth', 'Gate', 'Grade', 'Green', 'Grove', 'Heights', 'Hill', 'Knoll', 'Lane', 'Lawn', 'Loop', 'Mall', 'Manor', 'Mews', 'Mount', 'Nene', 'Nook', 'Oval', 'Park', 'Parkway', 'Passage', 'Path', 'Pathway', 'Pike', 'Place', 'Plaza', 'Promenade', 'Quadrant', 'Quay', 'Rise', 'Road', 'Route', 'Row', 'Spur', 'Square', 'Street', 'Terrace', 'Townline', 'Trace', 'Trail', 'Turnpike', 'Vale', 'Viaduct', 'View', 'Walk', 'Way'))

    street_number = str(randint(101,59999))
    st_name = choice(streets).strip('\n\r')
    street = street_number +' '+ st_name +' '+ street_type
    return street

def makeCity():
    f = open('us-zip_city_state.csv')
    cities = f.readlines()

    selected = choice(cities).strip('\n\r')
    selected = selected.split(',')
    city = (selected[1],selected[2],selected[0])
    return city


def makePhone():
    area = str(randint(100,999))
    prefix = str(randint(100,999))
    number = str(randint(1000,9999))

    phone = '('+area+')'+prefix+'-'+number

    return phone




