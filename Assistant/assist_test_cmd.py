import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
import pyttsx3

global engine
engine = pyttsx3.init()

#define the function to get the audio
def record_audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            assistant_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            assistant_speak('Sorry, I did not get that')
        except sr.RequestError:
            assistant_speak('Sorry, my speech service is down')
        return voice_data

#define the function to respond
def assistant_speak(audio_string):
    engine.say(audio_string)
    print(f"Computer: {audio_string}")
    engine.runAndWait()

#define the function to respond to the user's queries
def respond(voice_data):
    if 'what is your name' in voice_data:
        assistant_speak('My name is Assistant')
    if 'what time is it' in voice_data:
        assistant_speak(time.ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        assistant_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        assistant_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        assistant_speak('Goodbye')
        exit()

#start the program
time.sleep(1)
assistant_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)

time.sleep(1)
assistant_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)