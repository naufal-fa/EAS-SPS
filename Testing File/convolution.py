import numpy as np
import matplotlib as plt
import numpy.matlib
from scipy import signal

arr1 = np.array([2, 3, 4])
arr2 = np.array([1, 0, -6])

# Convolution
convres = np.convolve(arr1, arr2, 'same')
print('Convolution of {} and {} is {}'.format(arr1,arr2,convres))
convres = np.convolve(arr1, arr2)
print('Convolution of {} and {} is {}'.format(arr1,arr2,convres))
print('  ')