import queue as q
import sounddevice as sd
from vosk import Model as M
from vosk import KaldiRecognizer as KR
import pyttsx3 as pt3
import json
import datetime as dt
mdl = M("model")
rcgnzr = KR(mdl,16000)
audio_queue = q.Queue()
tts_engine = pt3.init()
def callback(indata,frames,time,status):
    if status:
        print(status)
    audio_queue.put(bytes(indata))
def process_query(query):
    query = query.lower()
    if "time" in query:
        now = dt.datetime.now().strftime("%H:%M:%S")
        rsp = f"The current time is {now}."
    elif "date" in query:
        today = dt.datetime.now().strftime("%A, %B %d, %Y")
        rsp = f"Today is {today}."
    elif "your name" in query:
        rsp = "I am your voice assistant, powered by Python."
    else:
        rsp = "I\'m sorry, I didn\'t understand that."
    print(f"Response : {rsp}")
    tts_engine.say(rsp)
    tts_engine.runAndWait()
def main():
    print("Listening...Speak into your microphone.")
    with sd.RawInputStream(samplerate = 16000,blocksize = 8000,dtype = "int16",channels = 1,callback = callback):
        while True:
            data = audio_queue.get()
            if rcgnzr.AcceptWaveform(data):
                rslt = rcgnzr.Result()
                txt = json.loads(rslt).get("text","")
                if txt:
                    print(f"You said : {txt}")
                    process_query(txt)
if __name__ == "__main__":
    main()