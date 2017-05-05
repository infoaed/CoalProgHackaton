# -*- coding: iso-8859-1 -*-
import re
import psycopg2
import datetime
import StringIO

class base():
	def __init__(self):
		self.wordDict = {}
		self.conn = psycopg2.connect(**base.ConnectionParams)

	def getBaseWord(self, word):
		return word
	
	def processText(self, text):
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
		'dbname': 'coalprog2',
		'user': 'postgres',
		'password': 'test',
		}
	
	def addToWordDict(self, tmpDict, syndmus_id):
		for key in tmpDict:
			if key not in self.wordDict:
				self.wordDict[key] = {}
			self.wordDict[key]['cnt'] = self.wordDict[key].get('cnt', 0) + tmpDict[key]['cnt']
			self.wordDict[key][syndmus_id] = tmpDict[key]['cnt']
			
	def initiate(self):
		tables = ["CREATE TABLE sonad (id serial PRIMARY KEY, cnt integer, sona varchar);",
					"CREATE TABLE sona_esinemine (sona varchar, syndmus_id integer, cnt integer);",
					"CREATE TABLE tmp_sonad (sona varchar, );",
					"CREATE TABLE tmp_syndmused (sona varchar, );"]
		for table in tables:
			try:
				cur = self.conn.cursor()
				cur.execute(table)
				cur.close()
			except Exception as msg:
				self.conn.rollback()
				print msg
		self.conn.commit()
			
			
	def process(self, dateFrom, dateTo):
		cur = self.conn.cursor()		
		cur.execute("""SELECT tekst, idsyndmus from public.syndmus where kuupaev > %s and kuupaev < %s""", (dateFrom, dateTo))
		rows = cur.fetchall()
		for row in rows:
			words = self.processText(row[0])
			self.addToWordDict(words, row[1])
				
		self.updateSonadDatabase()
		cur.execute("select COUNT(*) from sonad")
		print cur.fetchall()
		
	def updateSonadDatabase(self):
		cur = self.conn.cursor()
		
		cur.execute("DELETE from sonad")
		f = StringIO.StringIO()
		f2 = StringIO.StringIO()
		for key in self.wordDict:
			if not self.wordDict[key]['cnt']:
				continue
			f.write(str(self.wordDict[key]['cnt']) + '\t' + str(key) + '\n')
			for key2 in self.wordDict[key]:
				if key2 != 'cnt' and self.wordDict[key][key2]:
					f2.write(str(key) + '\t' + str(key2) + '\t' + str(self.wordDict[key][key2]) + '\n')
		f.seek(0)
		f2.seek(0)
		i = 0
		'''for line in f:
			i+=1
			if i > 7600 and i < 7700:
				print line
		i = 0
		for line in f2:
			i+=1
			if i > 54300 and i < 54400:
				print line'''
		cur.copy_from(f, 'sonad', columns=('cnt', 'sona'))
		cur.copy_from(f2, 'sona_esinemine', columns=('sona', 'syndmus_id', 'cnt'))
		self.conn.commit()
		
	def search(self, importantWords, words):
		cur = self.conn.cursor()
		
		baseWords = []
		f = StringIO.StringIO()
		cur.execute("delete from tmp_sonad")
		for word in words:
			f.write(self.getBaseWord(word) + '\n')
		f.seek(0)
		cur.copy_from(f, 'tmp_sonad', columns=['sona'])
		cur.execute("select sum(cnt) from sonad s, tmp_sonad ts where s.sona = ts.sona")
		print cur.fetchone()[0]
		cur.execute("""select s.total, ps.tekst from (select sum(se.cnt) as total, se.syndmus_id from sona_esinemine se, tmp_sonad ts where ts.sona = se.sona group by se.syndmus_id) s, public.syndmus ps where ps.idsyndmus = s.syndmus_id order by s.total asc""")
		
		rows = cur.fetchall()
		for row in rows:
			print (row[1] + '\n' + str(row[0]))
		
		
		
							
	
	def testProcessing(self):
		cur = self.conn.cursor()

		fromDate = datetime.date(2011, 4, 6) # Year, Month, Day
		toDate = datetime.date(2014, 3, 26) # Year, Month, Day
		#self.process(fromDate, toDate)
		self.search(['põhimõte', 'päevakord'])


if __name__ == '__main__':
	B = base()
	B.initiate()
	B.testProcessing()

