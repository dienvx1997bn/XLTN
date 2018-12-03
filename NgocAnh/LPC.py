from doctest import master

import numpy as np
import matplotlib.pyplot as plot
import scipy.signal as sg
import wave
from scipy import signal
# from master.scikits.talkbox.linpred.levinson_lpc import levinson,lpc
from scikits.talkbox.linpred.levinson_lpc import lpc
from scipy.io.wavfile import read
rate, signal = read("../Xe.wav")
signalA = []
for i in range(6000, 6512):
    signalA.append(signal[i])
signalA = np.array(signalA)
p = 14
a, e, k = lpc(signalA, p, -1)
a = np.append(a, np.zeros(512-14))
data_freq = np.fft.fft(a, 512)
data_freq = sg.resample(data_freq,512)
magSpectrum = np.abs(data_freq)
# magDb = 1/magSpectrum
magDb = -np.log(magSpectrum)
signalArray = []
signalDK = []
for k in range(6000, 6900):
    signalArray.append(signal[k])
signalArray = sg.resample(signalArray, 900)
for k in range(0, 149):  # day la K 0..150
    sig = 0
    for m in range(0, 299):
        sig = sig + np.abs(signalArray[m] - signalArray[ m - k])  # day la D(k)
    signalDK.append(sig)
# plot.plot(signalDK)
plot.subplot(311)
plot.plot(signalDK)
plot.subplot(312)
plot.plot(magDb)
plot.subplot(313)
plot.plot(magSpectrum)
plot.show()