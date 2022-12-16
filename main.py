import speech_recognition as sr
import pyttsx3
import playsound
import chat_gbt
import sys
import os

# Set the wakeword
WAKE_WORD = 'hey r2 hey r-2 hey r2d2 hey r2-d2 hey artoo-detoo hey artoo hairdo hey artoo detoo'

# Create a recognizer object
recognizer = sr.Recognizer()

# Create a microphone object
mic = sr.Microphone()

# Create a speaker output object
engine = pyttsx3.init()
engine.setProperty('rate', 140)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function to output text through speaker
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for the wakeword
def listen_for_wakeword():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)

    # Attempt to recognize the wakework
    try:
        text = recognizer.recognize_google(audio)
        if text.lower() in WAKE_WORD:
            return True
        else:
            return False
    except sr.UnknownValueError:
        playsound.playsound(os.path.join(os.path.dirname(__file__), 'audio/failureR2D2.mp3'))
        return False
    except sr.RequestError:
        playsound.playsound(os.path.join(os.path.dirname(__file__), 'audio/failureR2D2.mp3'))
        return False

# Start listening for the wakeword
while True:
    if listen_for_wakeword():
        # Once the wakeword is detected, start listening for commands
        playsound.playsound(os.path.join(os.path.dirname(__file__), 'audio/wakewordR2D2.mp3'))
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)

        # Attempt to recognize the command and get a response
        try:
            command = recognizer.recognize_google(audio)
            if command is not None:
                if command.lower() == "turn off":
                    playsound.playsound(os.path.join(os.path.dirname(__file__), 'audio/turnoffR2D2.mp3'))
                    engine.stop()
                    sys.exit()
                else:
                    response = chat_gbt.get_response(command)
                    speak(response)
        except sr.UnknownValueError:
            playsound.playsound(os.path.join(os.path.dirname(__file__), 'audio/failureR2D2.mp3'))
            pass
        except sr.RequestError:
            playsound.playsound(os.path.join(os.path.dirname(__file__), 'audio/failureR2D2.mp3'))
            pass
        except IndexError:
            playsound.playsound(os.path.join(os.path.dirname(__file__), 'audio/failureR2D2.mp3'))
            pass
