import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from soundPlay import soundPlay as sp

def gerarSinal():
    m = np.average([42921, 44615, 44619])/100
    Fs = 11024
    t = np.arange(-1, 1, 1/m)

    x = 3*np.cos(2*np.pi*Fs*t)

    plt.close('all')
    plt.title('$x(t)=A_1 \cos(2 \pi f_1 t) $')
    plt.plot(t, x)
    plt.grid(True)
    plt.xlabel('tempo $(s)$')
    plt.ylabel("Amplitude")
    plt.show()
    #sp(x,Fs)

gerarSinal()

