import numpy as np
import matplotlib.pyplot as plt

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
V_out = V_in * resistances / (resistances + R0)

# Plot hasil
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot tegangan (V_out)
ax1.plot(t, V_out, 'r-', label="Tegangan Keluar (V_out)", linewidth=2)
ax1.set_xlabel("Waktu (s)")
ax1.set_ylabel("Tegangan (V)", color='r')
ax1.tick_params(axis='y', labelcolor='r')

# Membuat sumbu kedua untuk suhu
ax2 = ax1.twinx()
ax2.set_ylabel("Suhu (°C)", color='b')  # Hanya label suhu, tanpa grafik
ax2.tick_params(axis='y', labelcolor='b')

# Mengatur rentang suhu sesuai dengan data suhu (suhu dalam Kelvin)
ax2.set_ylim(temperatures[0] - 273.15, temperatures[-1] - 273.15)  # Rentang suhu dalam °C

# Memberikan label dan grid
plt.title("NTC Thermistor 10K dengan Tegangan dan Suhu")
ax1.grid(True)

# Menampilkan legend
fig.tight_layout()
plt.show()
