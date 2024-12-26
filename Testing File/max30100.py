import numpy as np
import matplotlib.pyplot as plt
from dft import DFT

# Parameters
fs = 1000  # Sampling frequency (samples per second)
duration = 1  # Duration in seconds
heartbeat = 120 # Heart beat in BPM
f_heartbeat = heartbeat / 50  # Frequency of the heart beat in Hz
t = np.linspace(0, duration, int(fs * duration))
voltage_min = 1.8
voltage_max = 3.3
amplitude = (voltage_max - voltage_min) / 2
offset = (voltage_max + voltage_min) / 2

# Generate sinyal RED
signal1 = amplitude * np.sin(2 * np.pi * f_heartbeat * 2 * (t-1.8)) + offset
AC_red = signal1 + (np.max(signal1) - np.min(signal1))
DC_red = np.mean(signal1)

# Generate sinyal IR
signal2 = amplitude * np.sin(2 * np.pi * f_heartbeat * t) + offset
AC_ir = signal2 + (np.max(signal2) - np.min(signal2))
DC_ir = np.mean(signal2)

signal = (AC_red / DC_red) / (AC_ir / DC_ir)

# Plot hasil
plt.subplots(figsize=(10, 6))

# Plot tegangan (V_out)
plt.subplot(1, 1, 1)
plt.plot(t, signal, 'r-', label="MAX30102", linewidth=2)
plt.xlabel("Waktu (s)")
plt.ylabel("Tegangan (V)", color='r')
plt.tick_params(axis='y', labelcolor='r')
plt.legend()


plt.legend()
plt.grid()
plt.show()