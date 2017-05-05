import re


class base():
	
	def getBaseWord(word):
		return word
	
	def processText(text):
		words = re.split('. | |, |.\n', text)
		returnWords = {}
		for word in words:
			w = getBaseWord(word)
			returnWords[w]['cnt'] = returnWords[w].get('cnt', 0) + 1
			# lisa tegevused.
		return returnWords