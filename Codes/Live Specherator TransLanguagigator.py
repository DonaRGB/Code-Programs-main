import speech_recognition as sr
import pyttsx3 as ptx3
from googletrans import Translator as T
def speak(txt,language = "en"):
    engine = ptx3.init()
    engine.setProperty("rate",150)
    voices = engine.getProperty("voices")
    if language == "en":
        engine.setProperty("voice",voices[0].id)
    else:
        engine.setProperty("voice",voices[1].id)
    engine.say(txt)
    engine.runAndWait()
def speech_to_text():
    rcgnzr = sr.Recognizer()
    with sr.Microphone() as source:
        print("??? Please speak now in English...")
        audio = rcgnzr.listen(source)
    try:
        print("??? Recognizing speech... ")
        txt = r.recognize_google(audio,language = "en-US")
        print(f"✅ You said : {txt}")
        return txt
    except sr.UnknownValueError:
        print("❌ Error : Could not understand the audio")
    except sr.RequestError as e:
        print(f"❌ API Error : {e}")
    return None
def translate_text(txt,target_language = "es"):
    translator = T()
    translation = translator.translate(txt,target_language)
    print(f"??? Translated text : {translation.txt}")
    return translation.txt
def display_language_options():
    print("??? Available translation languages :\n 1.Hindi (hi)\n 2.Tamil (ta)\n 3.Telugu (te)\n 4.Bengali (bn)\n 5.Marathi (mr)\n 6.Gujarati (gu)\n 7.Malayalam (ml)\n 8.Punjabi (pa)")
    choice = str(input("Please select the target language number (1 - 8) : "))
    language_dict = {
        "1":"hi",
        "2":"ta",
        "3":"te",
        "4":"bn",
        "5":"mr",
        "6":"gu",
        "7":"ml",
        "8":"pa"
    }
    return language_dict.get(choice,"es")
def main():
    target_language = display_language_options()
    original_txt = speech_to_text()
    if original_txt:
        translated_txt = translate_text(original_txt,target_language = target_language)
        speak(translated_txt,language = "en")
        print("✅ Translation spoken out!")
if __name__ == "__main__":
    main()