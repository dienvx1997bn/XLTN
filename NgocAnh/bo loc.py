# tin hiệu + tin hiệu qua hamming + phổ biên độ + fig2 là hàm tương quan
from time import sleep

import numpy as np
import matplotlib.pyplot as plot
import scipy.signal as sg
import wave
from scipy.io.wavfile import read

rate, signal = read("../Xe.wav")
maxIndex = len(signal)
plot.figure()
for frames in range(0, 20):

    signalArray = []
    signalTQ = []
    for k in range(6000+frames*256, 6300+frames*256):
        signalArray.append(signal[k])
    signalArray = sg.resample(signalArray, 300)
    for k in range(0, 149):  # day la K 0..150
        sig = 0
        for y in range(0, 299 - k):
            sig = sig + signalArray[y] * signalArray[y + k]  # day la R(k)
        signalTQ.append(sig)

    plot.figure(1)
    plot.clf()
    # plot.subplot(111)
    plot.plot(signalTQ, color="purple")
    plot.grid(True)

    plot.figure(2)
    plot.clf()
    plot.subplot(311)
    signalCal = []
    for k in range(6000 + frames * 256, 6512 + frames * 256):
        signalCal.append(signal[k])
    signalCal = sg.resample(signalCal, 512)
    plot.plot(signalCal)
    plot.grid(True)

    plot.subplot(312)
    hamming512 = np.hamming(512)
    data = np.multiply(signalCal, hamming512)
    plot.plot(data)
    plot.grid(True)

    plot.subplot(313)
    data_freq = np.fft.fft(data, 512)
    magSpectrum = np.abs(data_freq)
    magDb = 20.0 * np.log10(magSpectrum / max(magSpectrum))
    # Frequency axe scalar
    ind = 255
    frequency = np.linspace(0, 1000, num=ind)
    plot.plot(frequency, magDb[0:ind], color='#00E100')

    plot.grid(True)
    plot.legend()

    plot.pause(1)
print(rate)
print(signalArray)
