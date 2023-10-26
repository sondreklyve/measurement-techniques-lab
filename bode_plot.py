#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

fontsize=14

arr = np.loadtxt("bode_plot_mikrofon.csv",
                 delimiter=",", dtype=float, skiprows=1)[:,0:2]

plt.figure(figsize=(20, 5))
plt.plot(arr[:,0],arr[:,1])
plt.xscale("log")
plt.title("Bode plot of dummy microphone circuit", fontsize=fontsize+4)
plt.xlabel("Frequency (Hz)", fontsize=fontsize)
plt.ylabel("Peak to Peak Voltage (V)", fontsize=fontsize)
plt.grid()
plt.savefig("Bode_plot_dummy_microphone.png")
plt.show()
