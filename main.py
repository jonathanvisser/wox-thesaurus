# -*- coding: utf-8 -*-
import json
import requests
from wox import Wox,WoxAPI


API_KEY = 'e68fda0b5edab0d6f3149502469d2810' # API key is available from here - http://words.bighugelabs.com/getkey.php
URL_MASK = 'http://words.bighugelabs.com/api/2/{1}/{0}/json'
RELATIONSHIP_ABBR = {'syn':'Synonyms','ant':'Antonyms','rel':'Related terms','sim':'Similar terms','usr':'User suggestions'}
#Your class must inherit from Wox base class https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
#The wox class here did some works to simplify the communication between Wox and python plugin.
class Thesaurus(Wox):
  def lookup_word(self,key):
    #WoxAPI.change_query(key)
    url = URL_MASK.format(key, API_KEY)

    r = requests.get(url)
    j = json.loads(r.text)
    return j
  def sizeFragments(self, results, wordtype,aWords,key,imagePath):
    # loop through array
    iRunningTotal = 0
    h = 0
    firstTimeFlag = True
    for i in range(0,len(aWords)):

      # count letters in word
      iRunningTotal = iRunningTotal + len(aWords[i])
      # if running total > 80 then create fragment array
      if (iRunningTotal > 70) or (i == len(aWords)-1):
        #print("h: " + str(h) + "   i: " + str(i))
        if firstTimeFlag == True:
          #print("FIRST TIME:")
          #print(aWords[h:i+1])
          self.addResult(results, wordtype,aWords[h:i+1],key,imagePath)
          firstTimeFlag = False
        else:
          imagePath = "Images/blank.ico"
          key =""
          wordtype = ""
          self.addResult(results, wordtype,aWords[h:i+1],key,imagePath)
          #print(aWords[h:i+1])
        h = i + 1
        iRunningTotal = 0
    

  def addResult(self, results, wordtype,words,key,imagePath):
    if key != "":
      key = RELATIONSHIP_ABBR[key]
    words = ', '.join(words)
    results.append({
      "Title": "{}{}".format(wordtype,words),
      "SubTitle": "{}".format(key),
      "IcoPath": imagePath
    })

  # A function named query is necessary, we will automatically invoke this function when user query this plugin
  def query(self,key):
    if len(key) > 2:
      results = []
      rex = self.lookup_word(key) # thesaurus Rex... geddit!?! :D
      # take the result set and break it up into result sets to append
      for key, value in rex.items(): # loop through word types
        previouswordtype = ""
        wordtype = key.upper() + ": "
        imagePath = "Images/syn.ico"
        for key, value in value.items(): # for each word type there maybe syn, ant, rel, sim, and user defined words
          words = value #', '.join(value)
          if previouswordtype == wordtype:
            wordtype = ""
            imagePath = "Images/" + key + ".ico"
          self.sizeFragments(results, wordtype,words,key,imagePath)

          #results.append({
          #  "Title": "{}{}".format(wordtype,words),
          #  "SubTitle": "{}".format(RELATIONSHIP_ABBR[key]),
          #  "IcoPath": imagePath
          #})
          previouswordtype = wordtype

      return results


#Following statement is necessary
if __name__ == "__main__":
  Thesaurus()