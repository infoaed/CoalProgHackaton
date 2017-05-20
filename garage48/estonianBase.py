from genericFunctions import base
from pyvabamorf import analyze #needs: pip install pyvabamorf
from pprint import pprint


class estonianBase(base):
	def getBaseWord(self, word):
		try:
			return analyze(word)[0]['analysis'][0]['lemma']
		except Exception as msg:
			pprint(word)
			print(analyze(word))
			print(msg)
	
	
if __name__ == '__main__':
	B = estonianBase()

	#B.initiate()
	#B.testProcessing()
	#B.process('2017-03-01 00:00:00', '2017-05-20 00:00:00')
	#B.process('2011-04-06 00:00:00', '2014-03-26 00:00:00')
	#B.process('1970-01-01 00:00:00', '2017-05-20 00:00:00')
	#B.search([('põhimõte', 1, 1), ('täname', 0, 3)], 1)
	print (B.findData(['metsaregister'], []))