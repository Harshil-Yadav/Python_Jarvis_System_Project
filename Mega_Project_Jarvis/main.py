import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognition = sr.Recognizer()
engine = pyttsx3.init("sapi5")



def speak(text):
    print("Speaking:", text)
    new_engine = pyttsx3.init()
    new_engine.say(text)
    new_engine.runAndWait()
    new_engine.stop()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Intialing Jarvis...") 
    while True:
        r = sr.Recognizer()

        # recognize 
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening")
                audio = r.listen(source, timeout=2, phrase_time_limit=5 )

            word = r.recognize_google(audio)
            print("You said:", word)

            if "jarvis" in word.lower():
                speak("Yes Boss")
                #listening for command
                with sr.Microphone() as source:
                    speak("Activating Jarvis...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                
                    processCommand(command)

        except Exception as e:
            print("error; {0}".format(e))

