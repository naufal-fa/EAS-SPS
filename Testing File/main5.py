import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 1000  # Sampling frequency (samples per second)
duration = 5  # Duration in seconds
f_heartbeat = 1.2  # Frequency of the heart beat in Hz
time_shift = 1.15  # Time shift for the second signal in seconds

# Time vector
t = np.linspace(0, duration, int(fs * duration))

# Generate the first sinusoidal signal
voltage_min = 1.8
voltage_max = 3.3
amplitude = (voltage_max - voltage_min) / 2
offset = (voltage_max + voltage_min) / 2
signal1 = amplitude * np.sin(2 * np.pi * 2.4 * t) + offset

# Generate the second sinusoidal signal with a time shift
t_shifted = t + time_shift
signal2 = amplitude * np.sin(2 * np.pi * 1.2 * t) + offset

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