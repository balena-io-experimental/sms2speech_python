#!/usr/bin/python

from flask import Flask, request, redirect
import twilio.twiml
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


app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
        """Respond to incoming calls with a simple text message."""
        sms = request.args.get('Body')
        print sms
        if not sms == "":
                print "ok"
                speakSpeechFromText(sms)

        resp = twilio.twiml.Response()
        #resp.message("Hello, Mobile Monkey")
        return str(resp)

if __name__ == "__main__":
        app.run( host='0.0.0.0', debug=True, port = 8080)

