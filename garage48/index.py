#!/usr/bin/python3

import cgitb
import cgi
from estonianBase import estonianBase
import json

cgitb.enable()
print("Content-Type: application/json; charset=utf-8\n\n")

form = cgi.FieldStorage()
mandatory = str(form.getvalue('mandatory')).split(',')
optional = str(form.getvalue('optional')).split(',')

#mandatory = ['metsaregister']
#optional = ['raieviiside']

Base = estonianBase()
data = Base.findData(mandatory, optional)

print (json.dumps(data))
