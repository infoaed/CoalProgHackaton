from genereicFunctions import base
from pyvabamorf import analyze #needs: pip install pyvabamorf


class estonianBase(base):
	def getBaseWord(self, word):
		return analyze(word)[0]['analysis'][0]['lemma']
	
	
	
B = estonianBase()

B.testProcessing()