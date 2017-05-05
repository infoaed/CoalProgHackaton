# -*- coding: utf-8 -*-

import re
import psycopg2
import datetime

class base():
	def __init__(self):
		self.wordDict = {}
		self.conn = psycopg2.connect(**base.ConnectionParams)

	def getBaseWord(self, word):
		return word
	
	def processText(self, text):
		print text
		words = re.split('[\.,!\?][ \n]| |[\(\)!\.\?]', text)
		print words
		returnWords = {}
		for word in words:
			if word == '':
				continue
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
			
	def initiate(self):
		cur = self.conn.cursor()
		cur.execute("CREATE TABLE sonad (id serial PRIMARY KEY, cnt integer, sona varchar);")
		cur.execute("CREATE TABLE sona_esinemine (sona_id serial, syndmus_id serial, cnt integer);")
		self.conn.commit()
			
			
	def process(self, dateFrom, dateTo):
		cur = self.conn.cursor()		
		cur.execute("""SELECT tekst from public.syndmus where kuupaev > %s and kuupaev < %s""", (dateFrom, dateTo))
		rows = cur.fetchall()
		for row in rows:
			self.addToWordDict(self.processText(row[0]))
		
	
	def testProcessing(self):
		cur = self.conn.cursor()

		fromDate = datetime.date(2010, 1, 1) # Year, Month, Day
		toDate = datetime.date(2011, 1, 1) # Year, Month, Day

		cur.execute("""SELECT tekst from public.syndmus where kuupaev > %s and kuupaev < %s LIMIT 4""", (fromDate, toDate))
		
		rows = cur.fetchall()
		for row in rows:
			self.addToWordDict(self.processText(row[0]))
		print str(self.wordDict)
		
B = base()
#B.initiate()
B.testProcessing()

