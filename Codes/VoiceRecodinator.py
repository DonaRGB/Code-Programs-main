import tkinter as tk
import sounddevice as sd
from scipy.io.wavfile import write as wr
sample_rate = 44100
duration = 5
def record_audio():
    status_label.config(text = "Recording...")
    window.update()
    audio = sd.rec(int(duration * sample_rate),samplerate = sample_rate,channels = 2)
    sd.wait()
    wr("output.wav",sample_rate,audio)
    status_label.config(text = "Recording saved as output.wav")
window = tk.Tk()
window.title("Voice Recorder")
record_btn = tk.Button(window,text = "Record",command = record_audio)
record_btn.pack(pady = 20)
status_label = tk.Label(window,text = "Press \"Record\" to start recording.")
status_label.pack(pady = 10)
window.mainloop()