import numpy as np 
import matplotlib.pyplot as plt 

# Generating the audio signal 
t = np.linspace(0, 1, 500, False) 
x = 0.5 * np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t) 

# Adding noise to the audio signal 
noise = np.random.normal(0, 1, len(x)) 
xn = x + noise 

# Plotting the audio signal before and after filtering 
plt.plot(t, xn, 'b', label='Noisy Signal') 
plt.legend() 
plt.show()