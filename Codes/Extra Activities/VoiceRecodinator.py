import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk as ttk
import numpy as np
import threading as thr
import sounddevice as sd
from scipy.io.wavfile import write as wr
from datetime import datetime as dt
sample_rate = 44100
MAX_DURATION = 24 * 3600
audio_data = None
is_paused = False
recording_thread = None
def disable_controls():
    hours_spinbox.config(state = "disabled")
    minutes_slider.config(state = "disabled")
    seconds_slider.config(state = "disabled")
    record_btn.config(state = "disabled")
def enable_controls():
    hours_spinbox.config(state = "normal")
    minutes_slider.config(state = "normal")
    seconds_slider.config(state = "normal")
    record_btn.config(state = "normal")
def update_minute_label(val):
    minute_value_label.config(text = f"{int(float(val))} min")
def update_seconds_label(val):
    second_value_label.config(text = f"{int(float(val))} sec")
def toggle_pause():
    global is_paused
    is_paused = not is_paused
    if is_paused:
        pause_btn.config(text = "⏯️ Resume")
        status_label.config(text = "Recording paused.")
    else:
        pause_btn.config(text = "⏸️ Pause")
        status_label.config(text = "Recording...")
def play_audio():
    global audio_data
    if audio_data is not None:
        sd.play(audio_data,samplerate = sample_rate)
def record_chunked_audio(total_seconds):
    global audio_data, is_paused
    chunk_size = 0.1
    num_chunks = int(total_seconds/chunk_size)
    audio_data = np.empty((int(total_seconds * sample_rate),2),dtype = np.float32)
    start_index = 0
    progress_bar["maximum"] = total_seconds
    progress_bar["value"] = 0
    progress_bar.pack(pady = 10)
    for _ in range(num_chunks):
        while is_paused:
            window.update()
        chunk = sd.rec(int(chunk_size * sample_rate),samplerate = sample_rate,channels = 2)
        sd.wait()
        end_idx = start_index + len(chunk)
        audio_data[start_index:end_idx] = chunk
        start_index = end_idx
        progress_bar["value"] += chunk_size
        window.update_idletasks()
    remaining_time = total_seconds - num_chunks * chunk_size
    if remaining_time > 0:
        while is_paused:
            window.update()
        chunk = sd.rec(int(remaining_time * sample_rate),samplerate = sample_rate,channels = 2)
        sd.wait()
        audio_data[start_index:] = chunk
        progress_bar["value"] = total_seconds
        window.update_idletasks()
    progress_bar.pack_forget()
    status_label.config(text = "Recording finished. You can ▶️ play or save it.")
def start_recording():
    global recording_thread, is_paused, audio_data
    disable_controls()
    try:
        hours = int(hours_spinbox.get())
        if hours < 0 or hours > 24:
            raise ValueError
    except ValueError:
        status_label.config(text = "Please enter a valid duration for hours (0 - 24)!")
        return
    minutes = minutes_slider.get()
    seconds = seconds_slider.get()
    total_seconds = 3600 * hours + minutes * 60 + seconds
    if total_seconds <= 0:
        status_label.config(text = "Recording duration must be greater than zero!")
        return
    if total_seconds > MAX_DURATION:
        status_label.config(text = "Total duration cannot exceed 24 hours!")
        return
    is_paused = False
    pause_btn.config(text = "⏸️ Pause")
    status_label.config(text = "Recording...")
    audio_data = None
    recording_thread = thr.Thread(target = record_chunked_audio,args = (total_seconds,))
    recording_thread.start()
    enable_controls()
def save_recording():
    global audio_data
    if audio_data is None:
        status_label.config(text = "No recording to save!")
        return
    timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
    default_fn = f"Recording_{timestamp}.wav"
    file_path = fd.asksaveasfilename(defaultextension = ".wav",initialfile = default_fn,filetypes = [("WAV files","*.wav")],title = "Save recording as...")
    if file_path:
        wr(file_path,sample_rate,audio_data)
        status_label.config(text = f"Recording saved in : {file_path}")
    else:
        status_label.config(text = "Recording canceled.")
def record_audio():
    try:
        hours = int(hours_spinbox.get())
        if hours < 0 or hours > 24:
            raise ValueError
    except ValueError:
        status_label.config(text = "Please enter a valid duration for hours (0 - 24)!")
        return
    minutes = minutes_slider.get()
    seconds = seconds_slider.get()
    duration = 3600 * hours + minutes * 60 + seconds
    if duration <= 0:
        status_label.config(text = "Recording duration must be greater than zero!")
        return
    if duration > MAX_DURATION:
        status_label.config(text = "Total duration cannot exceed 24 hours!")
        return
    status_label.config(text = "Recording...")
    window.update()
    audio = sd.rec(int(duration * sample_rate),samplerate = sample_rate,channels = 2)
    sd.wait()
    timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
    default_fn = f"Recording_{timestamp}.wav"
    file_path = fd.asksaveasfilename(defaultextension = ".wav",initialfile = default_fn,filetypes = [("WAV files","*.wav")],title = "Save recording as...")
    if file_path:
        wr(file_path,sample_rate,audio)
        status_label.config(text = f"Recording saved in : {file_path}")
    else:
        status_label.config(text = "Recording canceled.")
window = tk.Tk()
window.title("Voice Recorder")
tk.Label(window,text = "Hours (0 - 24):").pack()
hours_spinbox = tk.Spinbox(window,from_ = 0, to = 24, width = 5)
hours_spinbox.delete(0,"end")
hours_spinbox.insert(0,"0")
hours_spinbox.pack(pady = (0,10))
tk.Label(window,text = "Minutes :").pack()
minutes_slider = tk.Scale(window,from_ = 0, to = 59, orient = tk.HORIZONTAL, command = update_minute_label)
minutes_slider.pack()
minute_value_label = tk.Label(window, text = f"{minutes_slider.get()} min")
minute_value_label.pack(pady = (0,10))
tk.Label(window,text = "Seconds :").pack()
seconds_slider = tk.Scale(window,from_ = 0, to = 59, orient = tk.HORIZONTAL, command = update_seconds_label)
seconds_slider.set(5)
seconds_slider.pack()
second_value_label = tk.Label(window, text = f"{seconds_slider.get()} sec")
second_value_label.pack(pady = (0,10))
progress_bar = ttk.Progressbar(window,orient = tk.HORIZONTAL,length = 300,mode = "determinate")
record_btn = tk.Button(window,text = "⏺️ Record",command = start_recording)
record_btn.pack(pady = 5)
pause_btn = tk.Button(window,text = "⏸️ Pause",command = toggle_pause)
pause_btn.pack(pady = 5)
play_btn = tk.Button(window,text = "▶️ Play",command = play_audio)
play_btn.pack(pady = 5)
save_btn = tk.Button(window,text = "💾 Save",command = save_recording)
save_btn.pack(pady = 5)
status_label = tk.Label(window,text = "Set hours (0 - 24), minutes, and seconds, then press \"Record\".")
status_label.pack(pady = 10)
window.mainloop()