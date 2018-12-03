import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import wave
import scipy.signal as sg
from scipy import signal
from scikits.talkbox.linpred.levinson_lpc import lpc

spf = wave.open('XE.wav', 'r')
spf.setpos(9512)    # vi tri khung du lieu
signal = spf.readframes(512)
signal = np.fromstring(signal, 'Int16')

class SampleWaveFFT:

    def __init__(self):
        self.p = 14


        # self.r
        self.nfft = 512
        # Sampling Frequency
        self.rate = spf.getframerate()
        # Sine frequency
        self.F0 = self.rate / spf.getnframes()
        self.rate2 = self.F0 * self.nfft

    def create_signal(self):
        self.datasignal = np.zeros(self.nfft)
        # Timinig axe
        self.time = np.linspace(0, 2.0 * np.pi * self.F0 * self.nfft / self.rate, num=self.nfft)
        self.hamming = np.hamming(self.nfft)
        self.datasignal = sg.resample(signal, self.nfft)  # bo loc hieu chinh
        self.data = np.multiply(self.datasignal, self.hamming)

    def plot_signal(self):

        SMALL_SIZE = 14
        matplotlib.rc('font', size=SMALL_SIZE)
        matplotlib.rc('axes', titlesize=SMALL_SIZE)
        plt.subplot(412)
        plt.xlim(self.time[0], self.time[-1])
        plt.ylim(np.min(signal), np.max(signal))
        plt.fill_between(self.time, np.min(signal), np.max(signal), color='k')
        plt.plot(self.time, signal, color='#00E100')
        plt.grid(color='w')
        plt.xlabel('Time in second')
        plt.ylabel('Bien do')
        plt.subplot(413)
        plt.xlim(self.time[0], self.time[-1])
        plt.ylim(np.min(self.data), np.max(self.data))
        plt.fill_between(self.time, np.min(self.data), np.max(self.data), color='k')
        plt.plot(self.time, self.data, color='#00E100')
        plt.grid(color='w')
        plt.xlabel('Time in Second')
        plt.ylabel('Bien do')



    def _calculate_frequencies(self, data):
        data_freq = np.fft.fft(data, self.nfft)
        magSpectrum = np.abs(data_freq)
        self.magDb = 20.0 * np.log10(magSpectrum / max(magSpectrum))
        return self.magDb

    def plot_spectrum(self):
        plt.subplot(414)
        magDb = self._calculate_frequencies(self.data)
        minDb = min(magDb)
        maxDb = max(magDb)
        # Frequency axe scalar
        frequency = np.linspace(0, (self.rate2 / 2), num=(self.nfft) / 2 - 1)
        # Background in Black
        plt.fill_between(frequency, minDb, maxDb, color='k')
        ind = int(self.nfft / 2 - 1)
        plt.plot(frequency, magDb[0:ind], color='#00E100')
        plt.xlim(0, self.rate2 / 2.0)
        plt.ylim(minDb, maxDb)
        plt.grid(color='w')
        plt.xlabel('Frequency in Hz')
        plt.ylabel('Magnitude in  dB')

        plt.show()


    def LPC(self, frameh):           # error
        self.a, self.e, self.k = lpc(frameh, self.p, -1)
        self.a = np.append(self.a, np.zeros(self.nfft - self.p))


if __name__ == "__main__":

    specsin = SampleWaveFFT()
    creates = specsin.create_signal()
    drawsin = specsin.plot_signal()

    specsin.LPC(signal)

    plotspec = specsin.plot_spectrum()
