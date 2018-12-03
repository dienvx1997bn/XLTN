import numpy as np
import matplotlib.pyplot as plt
import matplotlib

nfft = 255
rate = 4000
F0 = 200
A = 87.56
u = 255
datasin = np.zeros(nfft)
time = np.linspace(0, 2.0 * np.pi * F0 * nfft / rate, num=nfft)
datasin = np.sin(time)
plt.figure(1)
plt.subplot(311)
plt.plot(time,datasin, color='#00E100')

plt.subplot(312)
y = []
# y = np.sign(datasin)
# y = np.abs((np.log(1+u*np.abs(datasin)))/(np.log(1+u)))
for k in range(0,254):
    if (datasin[k]>0):
        y.append(np.abs((np.log(1+u*np.abs(datasin[k])))/(np.log(1+u))))
    else :
        y.append(-np.abs((np.log(1+u*np.abs(datasin[k])))/(np.log(1+u))))
plt.plot(y)
plt.subplot(313)
ys= []
for k in range(0,254):
    if(datasin[k]>0):
        t = np.exp(y[k] * np.log(1 + u))
        z = (t - 1) / u
        ys.append(z)
    else:
        t = np.exp(-y[k] * np.log(1 + u))
        z = (t - 1) / u
        ys.append(-z)
plt.plot(ys)
plt.figure(2)
bacHinhSin = []
luongTuDeu = []
timeLuongTu = []
luongTuDeu.append(-1)
timeLuongTu.append(0)
for k in range(0, 17):
    bacHinhSin.append(-1+float(k)/7.5)
plt.subplot(211)
plt.plot(bacHinhSin)
for k in range(0, 254):
    # timeLuongTu.append(k)
    bien1 = 0
    bien2 = 0
    for x in range(0, 16):
        if((bacHinhSin[x]< datasin[k])&(bacHinhSin[x+1]> datasin[k])):
            bien1 = bacHinhSin[x]
            break
    for x in range(0, 16):
        if ((bacHinhSin[x]< datasin[k+1])&(bacHinhSin[x+1]> datasin[k+1])):
            bien2 = bacHinhSin[x]
            break
    timeLuongTu.append(k)
    timeLuongTu.append(k + 1)
    if(bien1 > bien2):
        luongTuDeu.append(bien1)
        luongTuDeu.append(bien1)
    else:
        luongTuDeu.append(bien2)
        luongTuDeu.append(bien2)
plt.subplot(212)
plt.plot(timeLuongTu,luongTuDeu)

# plt.plot(bacHinhSin)
# y = np.abs(y)
# y = []
# x = []
# data_freg = np.fft.fft(datasin,nfft)
# magSpectrum =np.abs(data_freg)
# magDb = 20.0* np.log10(magSpectrum / max(magSpectrum))
# ind = int(nfft / 2 - 1)
# frequency = np.linspace(0, (rate / 2), num=ind)
# plt.plot(frequency, magDb[0:ind], color='#00E100')
plt.show()