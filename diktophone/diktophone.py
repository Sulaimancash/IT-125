import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

import tkinter as tk
from tkinter import filedialog, messagebox
import threading

class Dictaphone:
    def __init__(self, sample_rate=44100, channels=1):
        self.sample_rate = sample_rate
        self.channels = channels
        self.audio_data = None
        self.is_recording = False
    
    def record(self, duration=None):
        self.is_recording = True
        print('Начата запись....')

        if duration:
            self.audio_data = sd.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=self.channels)
            sd.wait()
            self.is_recording = False
            print('Запись завершена')
        else:
            self.audio_data = []
            with sd.InputStream(samplerate=self.sample_rate, channels=self.channels, callback=self.callback):
                while self.is_recording:
                    sd.sleep(100)
    
    def callback(self, indata, frames, time, status):
        self.audio_data.append(indata.copy())
    
    def stop(self):
        self.is_recording = False
        if isinstance(self.audio_data, list):
            self.audio_data = np.concatenate(self.audio_data, axis=0)
        print('Запись остановлена')
    
    def save(self, filename='output.wav'):
        if self.audio_data is not None and len(self.audio_data) > 0:
            write(filename, self.sample_rate, (self.audio_data * 32767).astype(np.int16))
            print(f'Файл сохранен как: {filename}')
        else:
            print('Нет данных для сохранения....')

    def recognize_animal(self):
        if self.audio_data is None:
            return "Нет записи для анализа"

        data = self.audio_data.flatten()
        volume = np.max(np.abs(data))

        # Простая логика по амплитуде/длительности
        duration = len(data) / self.sample_rate
        avg_freq = np.mean(np.abs(np.fft.rfft(data)))

        # Примерные пороги для грубой классификации
        if volume > 0.2 and avg_freq < 500:
            return "Собака 🐶"
        elif volume > 0.1 and avg_freq > 500:
            return "Кот 🐱"
        else:
            return "Неизвестное животное"

class DictaphoneApp:
    def __init__(self, master):
        self.master = master
        master.title('Диктофон с распознаванием животных')
        master.geometry('640x420')

        self.dictaphone = Dictaphone()

        self.record_btn = tk.Button(master, text='Record', command=self.start_recording)
        self.record_btn.pack(pady=5)

        self.stop_btn = tk.Button(master, text='Stop', command=self.stop_recording)
        self.stop_btn.pack(pady=5)

        self.save_btn = tk.Button(master, text='Save', command=self.save_recording)
        self.save_btn.pack(pady=5)

        self.recognize_btn = tk.Button(master, text='Определить животное', command=self.recognize_animal)
        self.recognize_btn.pack(pady=5)

    def start_recording(self):
        thread = threading.Thread(target=self.dictaphone.record)
        thread.start()

    def stop_recording(self):
        self.dictaphone.stop()

    def save_recording(self):
        filename = filedialog.asksaveasfilename(defaultextension='.wav', filetypes=[("WAV files", '*.wav')])
        if filename:
            self.dictaphone.save(filename)

    def recognize_animal(self):
        result = self.dictaphone.recognize_animal()
        messagebox.showinfo("Распознавание", result)

if __name__ == '__main__':
    root = tk.Tk()
    app = DictaphoneApp(root)
    root.mainloop()
