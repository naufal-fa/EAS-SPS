import numpy as np
import matplotlib.pyplot as plt

R2 = 35  # Resistansi dari sensor 35k Ohm
V_in = 5 # Voltage Input sebesar 5V

def flex(sudut):
  R1 = 100 * (sudut / 180) + 35
  V_out = V_in * R1 / (R1+R2)
  return V_out

# Rentang sudut 0 - 180
sudut = np.linspace(0, 180, 1000)  # Dari 0θ hingga 150θ
t = np.linspace(0, 1, 1000)  # Rentang waktu, bisa disesuaikan

# Hitung tegangan keluaran
V_out = flex(sudut)

# Plot hasil
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot tegangan (V_out)
ax1.plot(t, V_out, 'r-', label="Tegangan Keluar (V_out)", linewidth=2)
ax1.set_xlabel("Waktu (s)")
ax1.set_ylabel("Tegangan (V)", color='r')
ax1.tick_params(axis='y', labelcolor='r')

# Membuat sumbu kedua untuk suhu
ax2 = ax1.twinx()
ax2.set_ylabel("Sudut (θ)", color='b')  # Hanya label suhu, tanpa grafik
ax2.tick_params(axis='y', labelcolor='b')

# Mengatur rentang sudut sesuai dengan data jurnal
ax2.set_ylim(sudut[0], sudut[-1])  # Rentang sudut dalam θ

# Memberikan label dan grid
plt.title("Flex Sensor dengan Tegangan dan Sudut")
ax1.grid(True)

# Menampilkan legend
fig.tight_layout()
plt.show()