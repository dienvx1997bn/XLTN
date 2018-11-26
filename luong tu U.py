import numpy as np
import matplotlib.pyplot as plt
import matplotlib

class SinFFT:
    def __init__(self):
        self.nfft = 512
        # Sampling Frequency
        self.rate = 4000
        # Sine frequency
        self.F0 = 50

    def create_sin(self):
        self.datasin = np.zeros(self.nfft)
        #Timinig axe
        self.time = np.linspace(0, 2.0 * np.pi * self.F0 * self.nfft / self.rate, num = self.nfft)
        self.datasin = np.sin(self.time)
        self.hamming = np.hamming(self.nfft)
        self.data = np.multiply(self.datasin, self.hamming)

    def plot_signal(self):
        SMALL_SIZE = 14
        matplotlib.rc('font', size = SMALL_SIZE)
        matplotlib.rc('axes', titlesize = SMALL_SIZE)
        plt.subplot(311)
        plt.xlim(self.time[0], self.time[-1])
        plt.ylim(np.min(self.datasin), np.max(self.datasin))
        plt.fill_between(self.time, np.min(self.datasin), np.max(self.datasin), color = 'k')
        plt.plot(self.time, self.datasin, color = '#00E100')
        plt.grid(color = 'w')
        plt.xlabel('Time in second')
        plt.ylabel('Bien do')

    def luongtu_u(self):
        self.r = np.zeros(512)

        for k in range(0,512):
            self.r[k] = np.sign(self.datasin[k])*np.log(1 + 255*abs(self.datasin[k])) / np.log(1 + 255)
            # self.r[k] = np.sign(self.input[k])*np.log(1 + 255*abs(self.input[k])) / np.log(1 + 255)
            # print(self.r[k])
        plt.subplot(312)
        plt.plot(self.r)

    def create(self):
        self.input = np.zeros(512)
        for k in range(0,512):
            self.input[k] = k

if __name__ == "__main__":
    specsin = SinFFT()
    creates = specsin.create_sin()
    drawsin = specsin.plot_signal()
    abc = specsin.create()
    luongtu = specsin.luongtu_u()
    plt.show()


