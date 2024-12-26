import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency (samples per second)
duration = 1  # Duration in seconds
heartbeat = 240 # Heart beat in BPM
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

# Plot the signals
plt.figure(figsize=(10, 6))
# plt.plot(t, signal1, label="Signal 1")
# plt.plot(t, signal2, label="Signal 2 (Time Shifted)", linestyle="--")
plt.plot(t, signal, label="Pulse Sensor", linestyle="--")
plt.title("Heart Beat Sinusoidal Signals")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.grid()
plt.show()