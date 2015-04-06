#!/usr/bin/python

import urllib, pycurl, os

def downloadFile(url, fileName):
    fp = open(fileName, "wb")
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, url)
    curl.setopt(pycurl.WRITEDATA, fp)
    curl.perform()
    curl.close()
    fp.close()

def getGoogleSpeechURL(phrase):
    googleTranslateURL = "http://translate.google.com/translate_tts?tl=en&"
    parameters = {'q': phrase}
    data = urllib.urlencode(parameters)
    googleTranslateURL = "%s%s" % (googleTranslateURL,data)
    return googleTranslateURL

def speakSpeechFromText(phrase):
    googleSpeechURL = getGoogleSpeechURL(phrase)
    downloadFile(googleSpeechURL,"tts.mp3")
    os.system("mplayer tts.mp3 -af extrastereo=0 &")
   
speakSpeechFromText("testing, testing, 1 2 3.")

