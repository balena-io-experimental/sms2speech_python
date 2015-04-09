This project allows to receive SMS sent to a Twilio number and then converts them into audible speech with google text-to-speech, on your Raspberry Pi.
#Step 1. List of materials

For this project we will be using:

- A Raspberry Pi (any version)
- Headphones or speakers
{<1>}![alt text](https://cloud.githubusercontent.com/assets/10128249/7073531/c0dc7616-defc-11e4-8d69-0e62194c7c03.jpg)

#Step 2: Create accounts

##Resin.io

Create an account in resin.io and follow the instructions on the “getting started guide", in order to be familiar with resin. Create an application e.g. “Twilio test” and select your device type, in our case it is a Raspberry Pi 2 (NOTE: Each Raspberry Pi model has its own device type, which you will need to select from the dropdown menu when creating your application, ensure you select the appropriate model). 

After you download and write the image on the SD card, your device will appear on resin’s dashboard. Then, select your device by clicking on it, go to “Actions” tab and then tick on the “Enable public URL for this device” box. We will use the generated URL later on Twilio.
{<2>}![alt text](https://cloud.githubusercontent.com/assets/10128249/7073532/c0e2cd9a-defc-11e4-880d-3656172f6e4d.gif)

##Twilio

Create an account in Twilio, it should be pretty straightforward. Go to “Numbers” and create one if you don’t have. You can test the new number by having Twilio send you a SMS or give you a call.

Click on the number and you should find a category called “messaging”. Then, select “Configure with URL”, paste the resin public URL on the Request URL (Make sure that you paste the link with the 8080 port), select the “HTTP GET method” and finally click on the save button at the end of the page. This way when a SMS is sent to Twilio, Twilio can notify us.    

{<3>}![alt text](https://cloud.githubusercontent.com/assets/10128249/7073533/c0e2ec3a-defc-11e4-8051-0a3a91cbd69c.gif)

#Step 3. Software

For the software we have to do two things, first listen for notification of incoming SMS from Twilio and then use Google translation text to speech. 

For the first part Twilio made a great job providing lots of tutorials and example code. I used an example that creates a server on the Raspberry pi with Flask that waits for incoming SMS messages and replies with a SMS to the number. In our case we didn’t need to reply so I removed it from the code. Resin exposes only port 8080 and 80 so we modified the code to listen on port 8080. 

```python
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
        """Respond to incoming calls with a simple text message."""
        sms = request.args.get('Body')
        if not sms == "":
                speakSpeechFromText(sms)
        resp = twilio.twiml.Response()
        return str(resp)

if __name__ == "__main__":
	print "Hello twilio"
    app.run( host='0.0.0.0', debug=True, port = 8080)
```

When we receive a valid incoming SMS, we simply parse the SMS message and then we sent them to the Google servers that converts the message to sound. From Google we download a mp3 file that contains the message and finally mplayer is used to play file. 
```python
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
```

If you have problems with getting the project to work, connect with Resin’s terminal session, use “cd app” and “python speech_test.py”. If you hear “testing, testing, 1 2 3.” that verifies that  Google text to speech and sound in the Raspberry works fine.
#Step 4. Connect the parts

Clone the project by running git clone https://github.com/nchronas/sms2speech.git, add the remote resin as seen in the Resin “getting started guide” and just git push resin master to upload the code to the device. It takes some time for the Raspberry Pi to download the code, but you can track the progress from your dashboard. In the meantime, you can make a coffee or a martini! If everything is ok, when you send a SMS to the twilio you should hear the lovely voice of google from the speakers.

##Resources


####Resin getting started:

http://flask.pocoo.org/docs/0.10/tutorial/

####Twilio example:

https://www.twilio.com/docs/quickstart/python/sms/hello-monkey

####Flask tutorial:

http://flask.pocoo.org/docs/0.10/tutorial/

####Google text to speech, python code

http://www.raspberrypi.org/forums/viewtopic.php?f=32&t=43379



