import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
xNum = 300
tNum = 500000
period = 2*pi
dt = 0.0001
delta = 0.022

energy = np.empty(xNum)

k = np.ndarray(xNum)
for i in range(0, xNum):
    k[i] = i - (i//(xNum/2))*xNum

# Discrete Fourier Transformation of sin(x)
x = np.linspace(0, period, xNum, endpoint=False)
discreteF = np.cos(x)
fftF = np.fft.fft(discreteF) / xNum

# Time Development of FFT(sin)
# Using the Runge-Kutta Method
for i in range(1, tNum):
    a = np.fft.ifft(1j*k*fftF) * xNum
    nonLinear = np.fft.fft( a * discreteF) / xNum
    fx =  delta**2 * 1j*k*k*k * fftF - nonLinear
    k1 = dt * fx
    k2 = dt * (delta**2 * 1j*k*k*k * (fftF + k1/2) - nonLinear)
    k3 = dt * (delta**2 * 1j*k*k*k * (fftF + k2/2) - nonLinear)
    k4 = dt * (delta**2 * 1j*k*k*k * (fftF + k3) - nonLinear)
    fftF = fftF + (k1 + 2*k2 + 2*k3 + k4) / 6
    discreteF = np.real(np.fft.ifft(fftF) * xNum)

    if i % 1000 == 0:
        plt.ylim(-1,3)
        plt.plot(x, discreteF)
        plt.savefig('./result2/result_t=%05d.png'%i)
        plt.cla()

energy = abs(fftF)**2 / 2