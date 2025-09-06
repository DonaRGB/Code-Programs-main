import pyaudio as pya
import speech_recognition as sr
import threading as thr
import time as t
import sys
from speech_recognition import AudioData as AD
stop_event = thr.Event()
def wait_for_enter():
    input("\nPress Enter to stop recording...\n")
    stop_event.set()
def spinner():
    spin_chars = "|/-\\"
    idx = 0
    while not stop_event.is_set():
        sys.stdout.write("\rRecording...  " + spin_chars[idx % len(spin_chars)])
        sys.stdout.flush()
        idx += 1
        t.sleep(0.1)
    sys.stdout.write("\rRecording stopped.             \n")
def record_unti_enter():
    p = pya.PyAudio()
    format = pya.paInt16
    channels = 1
    rate = 16000
    frames_per_buffer = 1024
    stream = p.open(rate,channels,format,True,frames_per_buffer = frames_per_buffer)
    frames = []
    thr.Thread(target = wait_for_enter).start()
    thr.Thread(target = spinner).start()
    while not stop_event.is_set():
        try:
            data = stream.read(frames_per_buffer)
            frames.append(data)
        except Exception as e:
            print(f"Error reading stream : {e}")
            break
    stream.stop_stream()
    stream.close()
    sample_width = p.get_sample_size(format)
    p.terminate()
    audio_data = b"".join(frames)
    return audio_data,rate,sample_width
def transcribe_audio(data,rate,width,filename = "transcription.txt",/):
    r = sr.Recognizer()
    audio = AD(data,rate,width)
    try:
        txt = r.recognize_google(audio)
    except sr.UnknownValueError:
        txt = "Could not understand the audio."
    except sr.RequestError as e:
        txt = f"API error : {e}"
    print(f"You said : \"{txt}\"")
    with open(filename,"w") as f:
        f.write(txt)
    print(f"Transcript saved to \"{filename}\"")
def main():
    print("??? Speak into the mic. Press Enter to stop.")
    audio,rate,width = record_unti_enter()
    transcribe_audio(audio,rate,width)
if __name__ == "__main__":
    main()