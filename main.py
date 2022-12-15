import speech_recognition
import pyttsx3
import response
import sys

WAKE_WORD = 'hey r2 hey r-2 hey r2d2 hey r2-d2 hey artoo-detoo hey artoo hairdo'
recognizer = speech_recognition.Recognizer()
speaker = pyttsx3.init('sapi5')

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()

            if text in WAKE_WORD:
                speaker.say('hello')
                speaker.runAndWait()
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()

                if text == 'turn off':
                    speaker.say('Beep Boop')
                    speaker.runAndWait()
                    speaker.stop()
                    sys.exit()
                else:
                    if text is not None:
                        res = response.get_chat_gpt_response(text)
                        speaker.say(res)
                        speaker.runAndWait()
    except speech_recognition.UnknownValueError:
        speaker.say('dunno!')
        speaker.runAndWait()
        recognizer = speech_recognition.Recognizer()
        pass
    except IndexError:
        speaker.say('dunno!')
        speaker.runAndWait()
        recognizer = speech_recognition.Recognizer()
        pass
