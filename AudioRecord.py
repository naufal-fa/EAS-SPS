import tkinter as tk
from tkinter import messagebox
import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class AudioRecorder:
    def __init__(self, master):
        self.master = master
        self.master.title("Audio Recorder")
        
        # Set window size to 1/2 of the screen
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        self.master.geometry(f"{screen_width // 2}x{screen_height // 2}")

        # Add title label
        title_label = tk.Label(master, text="Sistem Monitoring Untuk Analisis Suara Kebisingan Acara di Kawasan Perumahan\nGuna Memberikan Standar Batas Aman Penggunaan Audio", 
                                font=("Helvetica", 14), wraplength=screen_width // 2 - 20, justify="center")
        title_label.pack(pady=10)

        # Create a frame for buttons
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        # Create buttons in the same row
        self.record_button = tk.Button(button_frame, text="Record Sound", command=self.start_recording, font=("Helvetica", 12))
        self.record_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(button_frame, text="Stop Recording", command=self.stop_recording, font=("Helvetica", 12))
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.play_button = tk.Button(button_frame, text="Play Record", command=self.play_audio, font=("Helvetica", 12))
        self.play_button.pack(side=tk.LEFT, padx=5)

        # Create a figure for plotting
        self.fig, self.axs = plt.subplots(2, 1, figsize=(8, 8))  # Create 2 subplots
        self.line, = self.axs[0].plot([], [])
        self.axs[0].set_xlim(0, 44100)  # Set x-axis limit for audio signal
        self.axs[0].set_ylim(-1, 1)  # Set y-axis limit for audio signal
        self.axs[0].set_title("Audio Signal")
        self.axs[0].set_xlabel("Samples")
        self.axs[0].set_ylabel("Amplitude")

        # Create a canvas to embed the plot in the Tkinter window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()

        self.audio_data = None
        self.sample_rate = 44100  # Sample rate in Hz
        self.is_recording = False

    def start_recording(self):
        self.is_recording = True
        self.audio_data = []
        self.recording_stream = sd.InputStream(samplerate=self.sample_rate, channels=1, callback=self.audio_callback)
        self.recording_stream.start()
        self.update_plot()  # Start updating the plot

    def stop_recording(self):
        self.is_recording = False
        self.recording_stream.stop()
        self.recording_stream.close()
        messagebox.showinfo("Info", "Recording stopped!")
        self.plot_dft()  # Plot DFT after stopping the recording

    def audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.audio_data.append(indata.copy())

    def play_audio(self):
        if not self.audio_data:
            messagebox.showwarning("Warning", "No audio recorded!")
            return
        
        audio_array = np.concatenate(self.audio_data, axis=0)
        sd.play(audio_array, self.sample_rate)
        sd.wait()  # Wait until playback is finished
        messagebox.showinfo("Info", "Playback finished!")

    def update_plot(self):
        if self.is_recording:
            if self.audio_data:
                audio_array = np.concatenate(self.audio_data, axis=0)
                self.line.set_ydata(audio_array)
                self.line.set_xdata(np.arange(len(audio_array)))
                self.axs[0].set_xlim(0, len(audio_array))
                self.canvas.draw()  # Update the canvas
            self.master.after(100, self.update_plot)  # Update plot every 100 ms

    def plot_dft(self):
        if not self.audio_data:
            return
        
        audio_array = np.concatenate(self.audio_data, axis=0)
        # Compute DFT
        dft_result = np.fft.fft(audio_array.flatten())
        dft_magnitude = np.abs(dft_result)
        freqs = np.fft.fftfreq(len(dft_magnitude), 1/self.sample_rate)

        # Plot DFT in the second subplot
        self.axs[1].cla()  # Clear the previous plot
        self.axs[1].plot(freqs[:len(freqs)//2], dft_magnitude[:len(dft_magnitude)//2])  # Plot only the positive frequencies
        self.axs[1].set_title("DFT of Audio Signal")
        self.axs[1].set_xlabel("Frequency (Hz)")
        self.axs[1].set_ylabel("Magnitude")
        self.axs[1].grid()
        self.canvas.draw()  # Update the canvas to show the DFT plot

if __name__ == "__main__":
    root = tk.Tk()
    app = AudioRecorder(root)
    root.mainloop()