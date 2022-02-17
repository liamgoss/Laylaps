from re import T
import speech_recognition as sr
import pyttsx3, datetime, wikipedia, webbrowser, os, time, subprocess, wolframalpha, json, requests, sys
#https://towardsdatascience.com/how-to-build-your-own-ai-personal-assistant-using-python-f57247b4494b


if sys.platform == "darwin": # If running on mac
    engine=pyttsx3.init('nsss')
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.yuri')
    #for voice in engine.getProperty('voices'):
        #print(voice)
    #engine.setProperty('voice', f'com.apple.speech.synthesis.voice.{daniel}')

    

elif sys.platform == "win32": # If running on windows
    engine=pyttsx3.init('sapi5')

else: # If unsure of platform
    engine=pyttsx3.init('espeak')


'''
sapi5 - SAPI5 on Windows
nsss - NSSpeechSynthesizer on Mac OS X
espeak - eSpeak on every other platform
'''

# Microsoft Voice IDs
# Male:     HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0      => voices[0].id
# Female:   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0       => voices[1].id


# Define voice's properties
#engine.setProperty('voice', engine.getProperty('voices')[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop() # This can be removed I think






def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, good morning!")
    elif hour >= 12 and hour < 18:
        speak("Hello, good afternoon!")
    else:
        speak("Hello, good evening!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"You said: {statement}\n")
            speak(f"You said: {statement}")

        except Exception as e:
            speak("I didn't get that, please try again")
            return "None"
        return statement


# https://stackoverflow.com/questions/51992375/how-to-fix-installation-issues-for-pyaudio-portaudio-fatal-error-c1083-canno


if __name__ == '__main__':
    
    '''
    while True:
        speak("Say something!")
        statement = takeCommand().lower()
        if statement==0:
            continue
    '''
    speak("Testing")

