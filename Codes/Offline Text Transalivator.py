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
def callback(indata,status):
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
    else:
        rsp = "I\'m sorry, I didn\'t understand that."
    return rsp
with sd.RawInputStream():
    pass