from time import sleep
import speech_recognition as sr

morse_rep = {"a":[1, 2], "b": [2,1,1,1], "c":[2,1,2,1], "d": [2,1,1], "e": [1], "f": [1,1,2,1], "g": [2,2,1],
            "h":[1,1,1,1], "i": [1,1], "j": [1,2,2,2], "k": [2, 1, 2], "l": [1, 2, 1,1],
            "m": [2, 2], "n": [2, 1], "o": [2, 2, 2], "p": [1, 2, 2, 1], "q": [2, 2, 1, 2], "r": [1, 2, 1],
            "s": [1,1,1], "t": [2], "u": [1,1,2], "v":[1, 1, 1, 2], "w": [1,2,2], "x":[2, 1,1,2], "y":[2, 1, 2, 2],
            "z":[2, 2, 1, 1]}

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("say something: ")
    audio = recognizer.listen(source)
    try:
        word = recognizer.recognize_google(audio)
    except:
        print("sorry, I didn't understand")

print(word)
sep_word = list(word)

for i in sep_word:
    for j in morse_rep[i]:
        if j == 1:
            print("*")
        elif j == 2:
            print("**")
        sleep(0.7)
    sleep(1)
