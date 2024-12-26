import numpy as np
import matplotlib.pyplot as plt

# Parameters for the ultrasonic pulse
frequency = 40000  # Frequency of the ultrasonic pulse (40 kHz typical for HC-SR04)
duration = 0.001   # Duration of the pulse in seconds (1 ms)
sampling_rate = 400000  # Sampling rate (samples per second)

# Generate time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Generate the ultrasonic pulse signal (sinusoidal)
ultrasonic_pulse = np.sin(2 * np.pi * frequency * t)

# Plot the signal
plt.figure(figsize=(10, 4))
plt.plot(t, ultrasonic_pulse, label='Ultrasonic Pulse')
plt.title('Ultrasonic Pulse Signal (40 kHz)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.xlim(0, 0.00005)  # Zoom in to see the pulse clearly
plt.ylim(-1.1, 1.1)
plt.legend()
plt.show()