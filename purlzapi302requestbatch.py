#!user/bin/env python3


import requests

# Login information being passed
payload = {'id':'admin', 'passwd':'password'}

xml_file = 'purl_batch_test1.xml'

url_login = 'http://localhost:8080/admin/login/login-submit.bsh'
url_purls = 'http://localhost:8080/admin/purls'

#Opens and reads the xml file before being passed
xml = open(xml_file, 'r').read()

# Defines the content-type being passed
headers = {'Content-Type': 'application/xml'}

# Creates a request within a session to stay logged in when making multiple requests
with requests.Session() as s:
    r = s.post(url_login, data=payload)
    # check status code for response recieved 
    # success code - 200 
    print(r)
    # Give the object representing the XML file
    p = s.post(url_purls, data=xml, headers=headers)
    print(p)

