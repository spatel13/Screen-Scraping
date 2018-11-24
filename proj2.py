# Group 7
# Sara Nabulsi, Sahil Patel, Ujjwal Rehani, William Gao
# CMSC 491 - Social Media Mining
# 11/22/2018

import russell as ru
import requests 
import json
from bs4 import BeautifulSoup
import codecs
import nltk
import russell as ru

#parts 1 and 2
def removeUnicode(text):
	asciiText = ""
	for char in text:
		if(ord(char)<128):
			asciiText = asciiText + char
	return asciiText
	
fileObj = codecs.open("proj2.rtf","w","UTF")
html = requests.get("https://www.ecommercetimes.com/story/52616.html")
soup = BeautifulSoup(html.text,'html5lib')


#part3
all_paras = soup.find_all('p')

data_2018=""
for para in all_paras:
	fileObj.write(para.text)
	data_2018 = data_2018 + para.text
	
article_sum = ru.summarize(data_2018)

print "Summary of data mining article"
print "Three sentence summary"
for sent in article_sum['top_n_summary']:
	print removeUnicode(sent)

#part4
print "--------------------"
print "Bigrams:"
asc_2018 = removeUnicode(data_2018)
bigWords = nltk.tokenize.word_tokenize(asc_2018)
N = 25
search = nltk.BigramCollocationFinder.from_words(bigWords)
search.apply_freq_filter(2)
search.apply_word_filter(lambda skips: skips in nltk.corpus.stopwords.words('English'))

from nltk import BigramAssocMeasures
idxJaccard = BigramAssocMeasures.jaccard
bigrams = search.nbest(idxJaccard,N)

for bigram in bigrams:
	print str(bigram[0]).encode('utf-8')," ", str(bigram[1]).encode('utf-8')

	
	
	
	
