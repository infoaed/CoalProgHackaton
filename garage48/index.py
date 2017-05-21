#!/usr/bin/python3

import cgitb
import cgi
from estonianBase import estonianBase
import json
import hashlib
from pathlib import Path
from pprint import pprint

cgitb.enable()
print("Content-Type: application/json; charset=utf-8\n\n")

form = cgi.FieldStorage()
promise = str(form.getvalue('promise'))

if promise and promise != 'None':
	Base = estonianBase()
	promises = Base.findPromises()
	print(json.dumps(promises))
else:
	mandatory = str(form.getvalue('mandatory')).split(',')
	mandatory.sort()
	optional = str(form.getvalue('optional')).split(',')
	optional.sort()
	
	logFile = open('keywordlog.log', 'a+')
	logFile.write(str(form.getvalue('mandatory')) + '|' + str(form.getvalue('optional')) + '\n')
	logFile.close()

	cacheFileString = ','.join(mandatory) + ','.join(optional)
	cacheFileMd5 = hashlib.md5(cacheFileString.encode('utf-8')).hexdigest()
	cacheFilePath = 'cache/' + cacheFileMd5 + '.cache'
	file = Path(cacheFilePath)
	if not file.is_file():
		Base = estonianBase()
		data = Base.findData(mandatory, optional)
		jsonString = json.dumps(data)
		cacheFile = open(cacheFilePath, 'w+')
		cacheFile.write(jsonString)
		cacheFile.close()
		
	cacheFile = open(cacheFilePath)
	print(cacheFile.read())

