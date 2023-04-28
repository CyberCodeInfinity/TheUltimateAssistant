import speech_recognition as sr
from playsound import playsound

def main_mod_client():
    global r
    r = sr.Recognizer()




    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        playsound("./listening_sound.WAV")
        print("Listening...")
        audio = r.listen(source)

        try:
            print("Text From User: \n" + r.recognize_google(audio))

        except Exception as e:

            print("Error: " + str(e))


