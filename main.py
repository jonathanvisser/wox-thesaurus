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

  # A function named query is necessary, we will automatically invoke this function when user query this plugin
  def query(self,key):
    if len(key) > 2:
      results = []
      rex = self.lookup_word(key) # thesaurus Rex... geddit!?! :D
      # take the result set and break it up into result sets to append
      for key, value in rex.items(): # loop through word types
        previouswordtype = ""
        wordtype = key + ": "
        imagePath = "Images/syn.ico"
        for key, value in value.items(): # for each word type there maybe syn, ant, rel, sim, and user defined words
          words = ', '.join(value)
          if previouswordtype == wordtype:
            wordtype = ""
            imagePath = "Images/" + key + ".ico"
          wordslen = len(words)
     #     if wordslen > 90:
     #       linefragements =[]
     #       fragmentsneeded = int(wordslen/90)
     #       for i in range(0, fragmentsneeded):
     #         linefragements.append(words[0:90])
     #       for chunk in linefragements:
     #         results.append({
     #         "Title": "{}/{}:{}".format(wordslen,fragmentsneeded,chunk),
     #         "SubTitle": "In loop",
     #         "IcoPath": "Images/blank.ico"
     #     })
          results.append({
            "Title": "{}{}".format(wordtype,words),
            "SubTitle": "{}".format(RELATIONSHIP_ABBR[key]),
            "IcoPath": imagePath
          })
          previouswordtype = wordtype

      return results


#Following statement is necessary
if __name__ == "__main__":
  Thesaurus()