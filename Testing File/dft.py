import numpy as np

def DFT(x):
    N = len(x)
    X = [] # Sebagai tempat penyimpanan frequency

    # Membaca semua frequency pada signal
    for k in range(N):
        X_k = 0 # Fungsinya sebagai tempat penyimpanan amplitudo

        # Membaca semua sample pada input signal
        for n in range(N):
            e = np.exp(2j * np.pi * k * n / N) # Rumus DFT
            X_k += x[n] / e # Mencari frequency pada sample n

        X.append(X_k) # Memasukkan frequenc

    return np.array(X)
