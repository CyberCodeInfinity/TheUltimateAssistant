# This is an assistant that will answer any questions
# There may be more than one bugs (about 9% sure)

# *** *** START *** ***
import openai
import pyttsx3
from speech_client import main_mod_client
import speech_recognition as sr
from playsound import playsound

def assistant_module():
    engine = pyttsx3.init()

    def speak(audio):
        engine.say(audio)
        print(f"Computer: {audio}")
        engine.runAndWait()

    # Set up the OpenAI API client
    openai.api_key = "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"

    # Set up the model and prompt
    model_engine = "text-davinci-003"

    def client():
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

    while True:
        global r
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)

            playsound("./listen_sound_input.mp3")
            print("Listening...")
            audio = r.listen(source)
            playsound("./listen_sound_output.mp3")

            try:
                print("Text From User: \n" + r.recognize_google(audio))

            except Exception as e:

                print("Error: " + str(e))


        r = sr.Recognizer()
        prompt = r.recognize_google(audio)

        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text
        speak(response)

# *** *** END *** ***