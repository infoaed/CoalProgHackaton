# -*- coding: iso-8859-1 -*-
import re
import psycopg2
import datetime
#import StringIO
from io import StringIO
from pprint import pprint

class base():
	def __init__(self):
		self.wordDict = {}
		self.conn = psycopg2.connect(**base.ConnectionParams)

	def getBaseWord(self, word):
		return word
	
	def processText(self, text):
		text = text.replace(u'\xa0', u' ')
		words = re.split('[\.,!\?][ \n]| |[\(\)!\.\?\t\n<>]|<br/>', text)
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
		'dbname': 'valitsus',
		'user': 'postgres',
		'password': 'pass',
		}
	
	def addToWordDict(self, tmpDict, syndmus_id):
		for key in tmpDict:
			if key not in self.wordDict:
				self.wordDict[key] = {}
			self.wordDict[key]['cnt'] = self.wordDict[key].get('cnt', 0) + tmpDict[key]['cnt']
			self.wordDict[key][syndmus_id] = tmpDict[key]['cnt']
			
	def initiate(self):
		tables = ["CREATE TABLE sonad (id integer PRIMARY KEY, cnt integer, sona varchar);",
					"CREATE TABLE sona_esinemine (sona integer, syndmus_id integer, cnt integer);",
					"CREATE TABLE tmp_sonad (sona varchar, wordType integer, important integer );",
					"""CREATE FUNCTION multInt(integer, integer) RETURNS integer
					AS 'select $1 * $2;'
					LANGUAGE SQL
					IMMUTABLE
					RETURNS NULL ON NULL INPUT;
					"""
					"CREATE AGGREGATE mul(integer) ( SFUNC = multInt, STYPE=integer );",
					"CREATE INDEX sona_index ON sona_esinemine(sona);",
					"CREATE INDEX tmp_sona_index ON tmp_sonad(sona);"]
		for table in tables:
			try:
				cur = self.conn.cursor()
				cur.execute(table)
				cur.close()
				self.conn.commit()

			except Exception as msg:
				self.conn.rollback()
				print (msg)
			
			
	def process(self, dateFrom, dateTo):
		cur = self.conn.cursor()		
		cur.execute("""SELECT tekst, idsyndmus from public.syndmus where kuupaev > %s and kuupaev < %s""", (dateFrom, dateTo))
		rows = cur.fetchall()
		i = 0
		for row in rows:
			print('Processing row ' + str(i) + '/' + str(len(rows)))
			words = self.processText(row[0])
			self.addToWordDict(words, row[1])
			i = i + 1
				
		self.updateSonadDatabase()
		cur.execute("select COUNT(*) from sonad")
		print (cur.fetchall())
		
	def updateSonadDatabase(self):
		cur = self.conn.cursor()
		
		cur.execute("DELETE from sonad")
		f = StringIO()
		f2 = StringIO()
		i = 1
		for key in self.wordDict:
			if not self.wordDict[key]['cnt']:
				continue
			f.write(str(i) + '\t' + str(self.wordDict[key]['cnt']) + '\t' + str(key.encode('utf-8'), 'utf-8') + '\n')
			for key2 in self.wordDict[key]:
				if key2 != 'cnt' and self.wordDict[key][key2]:
					f2.write(str(i) + '\t' + str(key2) + '\t' + str(self.wordDict[key][key2]) + '\n')
			i = i + 1
		f.seek(0)
		f2.seek(0)

		cur.copy_from(f, 'sonad', columns=('id', 'cnt', 'sona'))
		cur.copy_from(f2, 'sona_esinemine', columns=('sona', 'syndmus_id', 'cnt'))
		self.conn.commit()
		
	def printAll(self, arr):
		for row in arr:
			print (str(row) + '\n')
		
	def search(self, words, importants):
		cur = self.conn.cursor()
		
		baseWords = []
		f = StringIO()
		cur.execute("delete from tmp_sonad")
		for word in words:
			f.write(self.getBaseWord(word[0]) + '\t' + str(word[1]) + '\t' + str(word[2]) + '\n')
		f.seek(0)
		cur.copy_from(f, 'tmp_sonad', columns=['sona', 'important', 'wordType'])
		cur.execute("select sum(cnt) from sonad s, tmp_sonad ts where s.sona = ts.sona")
		print (cur.fetchone()[0])
		
		'''
			Leian skoori iga s]na t[[biga. Seej'rel, n]uan k]igi important t[[pide olemasolu.
		

		cur.execute("""select sum(se.cnt) as cnt, ts.wordType, ts.important, se.syndmus_id from tmp_sonad ts, sona_esinemine se where ts.sona = se.sona  group by ts.wordType, ts.important, se.syndmus_id""")
		
		self.printAll(cur.fetchall())
		
		'''
		
		cur.execute("""select t.tekst, s.* from 
			
				(select sum(s.cnt) as total, sum(s.important) as totalImportants, s.syndmus_id from
			
				(select sum(se.cnt) as cnt, ts.wordType, ts.important, se.syndmus_id from sona_esinemine se, tmp_sonad ts where se.sona = ts.sona group by ts.wordType, ts.important, se.syndmus_id) 
				
				s group by s.syndmus_id) s
				
				, public.syndmus t where t.idsyndmus = s.syndmus_id and totalImportants >= %s order by total asc
			"""%(importants))
		
		rows = cur.fetchall()
		pprint(rows)
		for row in rows:
			print (str(row[0]) + '\n' + str(row[1]) + '\n' + str(row[2]))
		
	def findData(self, mandatory, optional):
		print ('paevakord.idpaevakord, syndmus.idsyndmus, sonad.sona, sona_esinemine.cnt, sonad.cnt \n')
		cur = self.conn.cursor()
		for i, word in enumerate(mandatory):
			mandatory[i] = self.getBaseWord(word)
		for i, word in enumerate(optional):
			optional[i] = self.getBaseWord(word)
		
		
		sql = '''SELECT paevakord.idpaevakord, syndmus.idsyndmus, sonad.sona, sona_esinemine.cnt, sonad.cnt
FROM paevakord
JOIN syndmus ON syndmus.paevakord_id=paevakord.idpaevakord
JOIN sona_esinemine ON sona_esinemine.syndmus_id=syndmus.idsyndmus
JOIN sonad ON sonad.id=sona_esinemine.sona'''
		
		allWords = mandatory + optional
		if len(allWords) > 0:
			sql = sql + ' WHERE (' + ' OR '.join(['sonad.sona=%s'] * len(allWords)) + ')'

		cur.execute(sql, allWords)
		rows = cur.fetchall()

		paevakords = dict()
		for row in rows:
			if not row[0] in paevakords:
				paevakords[row[0]] = {'rowdata': [], 'words': []}
			paevakords[row[0]]['rowdata'].append(row)
			paevakords[row[0]]['words'].append(row[2])
		
		for id in paevakords:
			paevakord = paevakords[id]
			valid = True
			for word in mandatory:
				if not word in paevakord['words']:
					valid = False
			if valid:
				for row in paevakord['rowdata']:
					print(row, '\n')
			
	
	def testProcessing(self):
		cur = self.conn.cursor()

		fromDate = datetime.date(2011, 4, 6) # Year, Month, Day
		toDate = datetime.date(2014, 3, 26) # Year, Month, Day
		#self.process(fromDate, toDate)
		self.search([('põhimõte', 1, 1), ('täname', 0, 3)], 1)#, ('päevakord', 0, 2)], 1)


if __name__ == '__main__':
	B = base()
	B.initiate()
	B.testProcessing()

