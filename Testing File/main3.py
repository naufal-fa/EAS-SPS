import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Variabel global untuk menyimpan nilai input
V_in = 5
heartbeat = 120
noise = 50

# Fungsi untuk mengubah konten di area konten ketika tombol di sidebar ditekan
def update_content(sensor_name):
    global V_in, heartbeat, noise  # Menggunakan variabel global

    # Menghapus konten sebelumnya
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    # Menampilkan nama sensor
    sensor_label = tk.Label(content_frame, text=f"Sinyal dari {sensor_name}", font=("Arial", 20, "bold"), bg="white")
    sensor_label.pack(pady=20)

    if sensor_name == "Flex Sensor" or "NTC Thermistor 10K":
        # Input untuk V_in
        inputlabel = tk.Label(content_frame, text="V_in (V):", bg="white", font=("Arial", 12))
        inputlabel.pack(pady=5)
        inputentry = tk.Entry(content_frame)
        inputentry.insert(0, str(V_in))
        inputentry.pack(pady=5)
    elif sensor_name == "Pulse Sensor" or "MAX30102":
        # Input untuk heartbeat
        input_label = tk.Label(content_frame, text="Heartbeat (BPM):", bg="white", font=("Arial", 12))
        input_label.pack(pady=5)
        input_entry = tk.Entry(content_frame)
        input_entry.insert(0, str(heartbeat))
        input_entry.pack(pady=5)

    # Input untuk noise
    noise_label = tk.Label(content_frame, text="Noise (Hz):", bg="white", font=("Arial", 12))
    noise_label.pack(pady=5)
    noise_entry = tk.Entry(content_frame)
    noise_entry.insert(0, str(noise))
    noise_entry.pack(pady=5)

    # Tombol untuk update plot
    update_button = tk.Button(content_frame, text="Update Plot", command=lambda: update_plot(sensor_name, input_entry.get(), noise_entry.get()), bg="#5DADE2", fg="white", font=("Arial", 14))
    update_button.pack(pady=10)

def update_plot(sensor_name, v_in_value, heartbeat_value):
    global V_in, heartbeat  # Menggunakan variabel global

    try:
        V_in = float(v_in_value)
        heartbeat = int(heartbeat_value)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Menghapus konten sebelumnya
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Membuat plot sinyal
    plot_signal(sensor_name, "Original")
    plot_signal(sensor_name, "Noise")
    plot_signal(sensor_name, "Discrete Fourier Transform")

    # Menampilkan nama sensor
    sensor_label = tk.Label(content_frame, text=f"Sinyal dari {sensor_name}", font=("Arial", 20, "bold"), bg="white")
    sensor_label.pack(pady=20)

    if sensor_name == "Flex Sensor" or "NTC Thermistor 10K":
        # Input untuk V_in
        inputlabel = tk.Label(content_frame, text="V_in (V):", bg="white", font=("Arial", 12))
        inputlabel.pack(pady=5)
        inputentry = tk.Entry(content_frame)
        inputentry.insert(0, str(V_in))
        inputentry.pack(pady=5)
    elif sensor_name == "Pulse Sensor" or "MAX30102":
        # Input untuk heartbeat
        input_label = tk.Label(content_frame, text="Heartbeat (BPM):", bg="white", font=("Arial", 12))
        input_label.pack(pady=5)
        input_entry = tk.Entry(content_frame)
        input_entry.insert(0, str(heartbeat))
        input_entry.pack(pady=5)

    # Input untuk noise
    noise_label = tk.Label(content_frame, text="Noise (Hz):", bg="white", font=("Arial", 12))
    noise_label.pack(pady=5)
    noise_entry = tk.Entry(content_frame)
    noise_entry.insert(0, str(noise))
    noise_entry.pack(pady=5)

    # Tombol untuk update plot
    update_button = tk.Button(content_frame, text="Update Plot", command=lambda: update_plot(sensor_name, input_entry.get(), noise_entry.get()), bg="#5DADE2", fg="white", font=("Arial", 14))
    update_button.pack(pady=10)

def plot_signal(sensor_name, plot_name):
    # Contoh data sinyal
    t = np.linspace(0, 1, 100)  # Waktu dari 0 hingga 1 detik
    if sensor_name == "Flex Sensor":
        R2 = 35  # Resistansi dari sensor 35k Ohm
        V_in = 5 # Voltage Input sebesar 5V

        def flex(sudut):
            R1 = 100 * (sudut / 180) + 35
            V_out = V_in * R1 / (R1 + R2)
            return V_out

        # Rentang sudut 0 - 180
        sudut = np.linspace(0, 180, 1000)  # Dari 0θ hingga 150θ
        t = np.linspace(0, 1, 1000)  # Rentang waktu, bisa disesuaikan
        # Hitung tegangan keluaran
        signal = flex(sudut)

        # Membuat figure dan axis untuk plot
        fig = Figure(figsize=(10, 2), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(t, signal, color='orange')
        ax.set_title(f"Sinyal {sensor_name} - {plot_name}", fontsize=16)
        ax.set_xlabel("Waktu (detik)", fontsize=12)
        ax.set_ylabel("Amplitudo", fontsize=12)

        # Membuat sumbu kedua untuk suhu
        ax2 = ax.twinx()
        ax2.set_ylabel("Sudut (θ)", color='blue', fontsize=12)  # Hanya label suhu, tanpa grafik
        ax2.tick_params(axis='y', labelcolor='blue')

        # Mengatur rentang sudut sesuai dengan data jurnal
        ax2.set_ylim(sudut[0], sudut[-1])  # Rentang sudut dalam θ
    elif sensor_name == "NTC Thermistor 10K":
        # Parameter sensor
        R0 = 10000  # Resistansi pada suhu referensi (ohm)
        beta = 3550  # Konstanta material
        T0 = 298  # Suhu referensi (Kelvin)
        V_in = 5 # Voltage Input sebesar 5V

        def thermistor(T):
            R = R0 * np.exp(beta * (1/T - 1/T0))
            return R

        # Rentang suhu
        temperatures = np.linspace(273, 423, 1000)  # Dari 0°C hingga 150°C
        t = np.linspace(0, 1, 1000)  # Rentang waktu, bisa disesuaikan

        # Hitung resistansi untuk setiap suhu
        resistances = thermistor(temperatures)

        # Hitung tegangan keluaran
        signal = V_in * resistances / (resistances + R0)

        # Membuat figure dan axis untuk plot
        fig = Figure(figsize=(10, 2), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(t, signal, color='green')
        ax.set_title(f"Sinyal {sensor_name} - {plot_name}", fontsize=16)
        ax.set_xlabel("Waktu (detik)", fontsize=12)
        ax.set_ylabel("Amplitudo", fontsize=12)

        # Membuat sumbu kedua untuk suhu
        ax2 = ax.twinx()
        ax2.set_ylabel("Suhu (°C)", color='blue', fontsize=12)  # Hanya label suhu, tanpa grafik
        ax2.tick_params(axis='y', labelcolor='blue')
        # Mengatur rentang suhu sesuai dengan data suhu (suhu dalam Kelvin)
        ax2.set_ylim(temperatures[0] - 273.15, temperatures[-1] - 273.15)  # Rentang suhu dalam °C
    elif sensor_name == "Pulse Sensor":
        # Parameters
        fs = 1000  # Sampling frequency (samples per second)
        duration = 1  # Duration in seconds
        heartbeat = 120  # Heart beat in BPM
        f_heartbeat = heartbeat / 50  # Frequency of the heart beat in Hz

        # Time vector
        t = np.linspace(0, duration, int(fs * duration))

        # Generate the first sinusoidal signal
        voltage_min = 1.8
        voltage_max = 3.3
        amplitude = (voltage_max - voltage_min) / 2
        offset = (voltage_max + voltage_min) / 2

        signal1 = amplitude * np.sin(2 * np.pi * f_heartbeat * 2 * t) + offset
        signal2 = amplitude * np.sin(2 * np.pi * f_heartbeat * t) + offset
        signal = signal1 / signal2

        # Membuat figure dan axis untuk plot
        fig = Figure(figsize=(10, 2), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(t, signal, color='red')
        ax.set_title(f"Sinyal {sensor_name} - {plot_name}", fontsize=16)
        ax.set_xlabel("Waktu (detik)", fontsize=12)
        ax.set_ylabel("Amplitudo", fontsize=12)
    elif sensor_name == "MAX30102":
        # Parameters
        fs = 1000  # Sampling frequency (samples per second)
        duration = 1  # Duration in seconds
        heartbeat = 120  # Heart beat in BPM
        f_heartbeat = heartbeat / 50  # Frequency of the heart beat in Hz
        t = np.linspace(0, duration, int(fs * duration))
        voltage_min = 1.8
        voltage_max = 3.3
        amplitude = (voltage_max - voltage_min) / 2
        offset = (voltage_max + voltage_min) / 2

        # Generate sinyal RED
        signal1 = amplitude * np.sin(2 * np.pi * f_heartbeat * 2 * (t - 1.8)) + offset
        AC_red = signal1 + (np.max(signal1) - np.min(signal1))
        DC_red = np.mean(signal1)

        # Generate sinyal IR
        signal2 = amplitude * np.sin(2 * np.pi * f_heartbeat * t) + offset
        AC_ir = signal2 + (np.max(signal2) - np.min(signal2))
        DC_ir = np.mean(signal2)

        signal = (AC_red / DC_red) / (AC_ir / DC_ir)

        # Membuat figure dan axis untuk plot
        fig = Figure(figsize=(10, 2), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(t, signal, color='purple')
        ax.set_title(f"Sinyal {sensor_name} - {plot_name}", fontsize=16)
        ax.set_xlabel("Waktu (detik)", fontsize=12)
        ax.set_ylabel("Amplitudo", fontsize=12)
    else:
        signal = np.zeros(100)  # Sinyal nol

        # Membuat figure dan axis untuk plot
        fig = Figure(figsize=(10, 2), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot(t, signal, color='gray')
        ax.set_title(f"Sinyal {sensor_name} - {plot_name}", fontsize=16)
        ax.set_xlabel("Waktu (detik)", fontsize=12)
        ax.set_ylabel("Amplitudo", fontsize=12)

    # Menampilkan plot di Tkinter
    canvas = FigureCanvasTkAgg(fig, master=content_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=10)

# Fungsi untuk menghitung lebar sidebar (1 /4 dari lebar root)
def resize_sidebar(event):
    sidebar_width = int(root.winfo_width() / 4)
    sidebar.config(width=sidebar_width)
    # Menyesuaikan konten frame dengan lebar baru
    

# Membuat root window
root = tk.Tk()

# Mengatur root window menjadi fullscreen windowed
root.attributes('-fullscreen', True)
root.state('normal')  # Membuat window menjadi dapat diresize

# Membuat frame untuk sidebar dengan lebar awal yang nanti akan disesuaikan
sidebar = tk.Frame(root, bg="#4A90E2", height=600, relief="sunken")
sidebar.pack(side="left", fill="y")

# Menambahkan logo atau teks di atas sidebar
logo_label = tk.Label(sidebar, text="Sistem Pengolahan Sinyal", font=("Arial", 22, "bold"), bg="#4A90E2", fg="white")
logo_label.pack(pady=20, padx=10)

# Membuat frame untuk konten
content_frame = tk.Frame(root, bg="white", height=600)
content_frame.pack(side="right", fill="both", expand=True)

# Menambahkan tombol-tombol di sidebar
sidebar_button1 = tk.Button(sidebar, text="Flex Sensor", command=lambda: update_content("Flex Sensor"), bg="#5DADE2", fg="white", font=("Arial", 14))
sidebar_button1.pack(pady=10, padx=10, fill="x")

sidebar_button2 = tk.Button(sidebar, text="NTC Thermistor 10K", command=lambda: update_content("NTC Thermistor 10K"), bg="#5DADE2", fg="white", font=("Arial", 14))
sidebar_button2.pack(pady=10, padx=10, fill="x")

sidebar_button3 = tk.Button(sidebar, text="Pulse Sensor", command=lambda: update_content("Pulse Sensor"), bg="#5DADE2", fg="white", font=("Arial", 14))
sidebar_button3.pack(pady=10, padx=10, fill="x")

sidebar_button4 = tk.Button(sidebar, text="MAX30102", command=lambda: update_content("MAX30102"), bg="#5DADE2", fg="white", font=("Arial", 14))
sidebar_button4.pack(pady=10, padx=10, fill="x")

sidebar_button5 = tk.Button(sidebar, text="Tombol 5", command=lambda: update_content("Tombol 5"), bg="#5DADE2", fg="white", font=("Arial", 14))
sidebar_button5.pack(pady=10, padx=10, fill="x")

# Menambahkan tombol Exit di bagian bawah sidebar
exit_button = tk.Button(sidebar, text="Exit App", command=root.quit, bg="red", fg="white", font=("Arial", 14))
exit_button.pack(side="bottom", pady=10, padx=10, fill="x")

# Label untuk menampilkan konten di area konten
content_label = tk.Label(content_frame, text="Selamat datang! Pilih tombol di sidebar untuk melihat sinyal sensor", font=("Arial", 16), bg="white")
content_label.pack(pady=20)

# Menghubungkan event resize window agar lebar sidebar sesuai
root.bind("<Configure>", resize_sidebar)

# Menjalankan aplikasi
root.mainloop()