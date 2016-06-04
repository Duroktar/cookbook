#!/usr/bin/env python3
import speech_recognition as sr
import pyaudio
# NOTE: this example requires PyAudio because it uses the Microphone class

index = pyaudio.PyAudio().get_default_input_device_info()
print index

myPyAudio=pyaudio.PyAudio()
print "Seeing pyaudio devices:",myPyAudio.get_device_count()

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(1) as source:
    print("Say something!")
    audio = r.listen(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))