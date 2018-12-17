import numpy as np
from matplotlib.pyplot import stem
import matplotlib.pyplot as plt
from scipy.signal import (freqz, tf2zpk, lfilter)

class ABC:
    def __init__(self):
        Fk = 1000.0
        Bk = 100.0
        self.Fs = 10000.0

        Ts = 1/self.Fs
        Sicmak = np.pi * Bk
        Thetak = 2*np.pi*Fk*Ts
        Zk = np.exp(-Sicmak*Ts)
        b0 = 1-2.0*Zk*np.cos(Thetak) + Zk*Zk
        self.b = [b0,0,0]
        a0 = 1
        a1 = -2*Zk*np.cos(Thetak)
        a2 = Zk*Zk
        self.a = [a0,a1,a2]

    def result(self):
        print(self.a)
        print(self.b)

    # tinh diem cuc diem 0
    def tinhDiemCuc(self):
        z,p,k = tf2zpk(self.b,self.a)
        # print("z = "  + z + "\tp = " + p + "\tk = " + k)

        #ve dap ung xung
    def VeDapUngXung(self):
        index = np.arange(0, 20)
        #tao xung don vi
        u = 1.0 * (index == 0)
        #
        y = lfilter(self.b, self.a, u)
        plt.subplot(211)
        stem(index, y)

    def VeDapUngBienDo(self):
        w, h = freqz(self.b, self.a)
        #truc tan so theo Hz
        f = np.linspace(0, self.Fs / 2, num=len(h))
        #dap ung bien do theo DB
        H = np.log10(abs(h))

        plt.subplot(212)
        plt.plot(f, H)




if __name__ == "__main__":
    init = ABC()
    show = init.result()
    diemcuc = init.tinhDiemCuc()
    show = init.VeDapUngXung()
    show2 = init.VeDapUngBienDo()
    plt.show()






