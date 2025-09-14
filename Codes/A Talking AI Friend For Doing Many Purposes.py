import speech_recognition as sr
import pyttsx3 as pt3
from datetime import datetime as dt
import requests as rqs
engine = pt3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.setProperty("rate",150)
username = ""
def speak(txt):
    engine.say(txt)
    engine.runAndWait()
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("??? Speak now...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"✅ You said : {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Could not understand")
            speak("Sorry, I didn\'t catch that.")
        except sr.RequestError as e:
            print(f"❌ API Error : {e}")
            speak("There was a network issue.")
    return ""
def grtf():
    url = r"https://uselessfacts.jsph.pl/random.json?language=en"
    rsp = rqs.get(url)
    if rsp.status_code == 200:
        fd = rsp.json()
        return f"Did you know that {fd['text'].lower()}?"
    else:
        return "Failed to fetch fact"
def respond_to_command(command):
    global username
    if "hello" in command:
        if username:
            speak(f"Hi {username}, how can I help you?")
        else:
            speak("Hi there! How can I help you?")
    elif "your name" in command:
        speak("I am your smart AI assistant.")
    elif "time" in command:
        now = dt.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}.")
    elif "date" in command:
        today = dt.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is the {today}.")
    elif "my name is" in command:
        username = command.split("my name is")[-1].strip().capitalize()
        speak(f"Nice to meet you, {username}")
    elif "fact" in command:
        fact = grtf()
        speak(fact)
    elif "use male voice" in command:
        engine.setProperty("voice",voices[0].id)
        speak("Switched to male voice")
    elif "use female voice" in command:
        engine.setProperty("voice",voices[1].id)
        speak("Switched to female voice")
    elif "stop" in command or "exit" in command or "leave" in command:
        speak("Goodbye")
        return False
    else:
        speak("I\'m not sure how to help with that.")
    return True
def main():
    speak("Voice assistant activated. Say something!")
    while True:
        command = get_audio()
        if command and not respond_to_command(command):
            break
if __name__ == "__main__":
    main()