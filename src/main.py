import speech_recognition as sr
import pyttsx3, datetime, wikipedia, webbrowser, os, time, subprocess, wolframalpha, json, requests
#https://towardsdatascience.com/how-to-build-your-own-ai-personal-assistant-using-python-f57247b4494b


engine=pyttsx3.init('sapi5')
'''
sapi5 - SAPI5 on Windows
nsss - NSSpeechSynthesizer on Mac OS X
espeak - eSpeak on every other platform
'''
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Testing testing 1 2 3")