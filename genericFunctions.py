# -*- coding: utf-8 -*-

import re
import psycopg2
import datetime

class base():
	def __init__(self):
		self.wordDict = {}
	
	def getBaseWord(self, word):
		return word
	
	def processText(self, text):
		words = re.split('. | |, |.\n', text)
		returnWords = {}
		for word in words:
			w = self.getBaseWord(word)
			if w not in returnWords:
				returnWords[w] = {}
			returnWords[w]['cnt'] = returnWords[w].get('cnt', 0) + 1
			# lisa tegevused.
		return returnWords
	
	ConnectionParams = {
		'dbname': 'coalprog2',
		'user': 'postgres',
		'password': 'test',
		}
	
	def addToWordDict(self, tmpDict):
		for key in tmpDict:
			if key not in self.wordDict:
				self.wordDict[key] = {}
			self.wordDict[key]['cnt'] = self.wordDict[key].get('cnt', 0) + tmpDict[key]['cnt']
			
	
	def testProcessing(self):
		conn = psycopg2.connect(**base.ConnectionParams)
		cur = conn.cursor()

		fromDate = datetime.date(2010, 1, 1) # Year, Month, Day
		toDate = datetime.date(2011, 1, 1) # Year, Month, Day

		cur.execute("""SELECT tekst from public.syndmus where kuupaev > %s and kuupaev < %s LIMIT 10""", (fromDate, toDate))
		
		rows = cur.fetchall()
		for row in rows:
			self.addToWordDict(self.processText(row[0]))
		print str(self.wordDict)
		
B = base()
B.testProcessing()
		
	
