import speech_recognition as sr
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import gtts
from playsound import playsound

print("""
1.audio to text
2.text to audio
""")

choose = int(input())
if choose == 1:
    #make instance of class Recognizer, which helps to convert speech to text
    recognizer=sr.Recognizer()
    print(""""
    1.choose a path
    2.record an audio
    """)

    number = int(input())
    # python-version is 3.7 ,and it doesn't support match-case
    if number == 1:
            Tk().withdraw()
            filepath = askopenfilename()
            #open the file
            with sr.AudioFile(filepath) as sourse:
                #listen the data
                audio = recognizer.record(sourse)
                text=recognizer.recognize_google(audio)
                print(text)
    elif number == 2:
        with sr.Microphone() as source:
            audio = recognizer.record(source, duration=5)
            text = recognizer.recognize_google(audio)
            print(text)
    else:
        print("wrong number !")


elif choose == 2:
    tts = gtts.gTTS(input("enter the text : "))
    tts.save("audio_file.mp3")
    playsound("audio_file.mp3")


else:
    print("wrong number !")