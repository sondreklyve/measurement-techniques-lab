#!/usr/bin/env python3
import sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 5:
    print("Too few arguments, please enter all of the following:")
    print("\t-filename")
    print("\t-plot title")
    print("\t-plot type (P2P, Phase)")
    print("\t-save figure (y/n)")
    exit()
if len(sys.argv) > 5:
    print("Error: Too many arguments")
    exit()


filename = sys.argv[1]
print(filename)
plot_title = sys.argv[2]
plot_type = sys.argv[3]
save_fig = (sys.argv[4] == "y")

fontsize=14

arr = np.loadtxt(filename,
                 delimiter=",", dtype=float, skiprows=1)[:,0:2]

plt.figure(figsize=(15, 7))
plt.plot(arr[:,0],arr[:,1])
plt.xscale("log")
plt.title(plot_title, fontsize=fontsize+4)
plt.xlabel("Frequency (Hz)", fontsize=fontsize)
if plot_type == "P2P":
    plt.ylabel("Peak to Peak Voltage (V)", fontsize=fontsize)
elif plot_type == "Phase":
    plt.ylabel("Phase (deg)", fontsize=fontsize)
else:
    print("Plot type not recognized")
    exit()

plt.grid()
if save_fig:
    plt.savefig(filename[0:-3]+"png")
plt.show()
