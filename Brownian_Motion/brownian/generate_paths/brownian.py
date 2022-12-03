# MatPlotLib
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import math

def brownian_motion_path(t,n):
    plt.figure(facecolor="#c8f70c39")
    ax = plt.axes()
    ax.set_facecolor("black")

    t = float(t)
    n = int(n)
    Wcum = []
    ti = np.linspace(0,t,10000)
    
    for k in range(n):
        R =[]
        V = []
        u = []
        N = 10000
        z1 = []
        z2 = []
        z = []
        for i in range(N):
            u1 = np.random.random()
            u2 = np.random.random()
            R.append(-2 * math.log(u1))
            V.append(2 * math.pi * u2)
            z1.append(np.sqrt(R[i]) * np.cos(V[i]))
            z2.append(np.sqrt(R[i]) * np.sin(V[i]))
            u.append(u1)
            u.append(u2)


        for i in range(len(z1)):
            z.append(z1[i])
            z.append(z2[i])


        u = []
        for i in range(4999):
            ui = np.random.uniform()
            u.append(ui)

        ui = np.random.uniform()
        u.append(ui)
        W = []
        W.append(0)
        for j in range(9999):
            W.append(W[j] + math.sqrt(ti[j+1] - ti[j])*z[j] )
        Wcum.append(W)


    for i in range(n):
        plt.plot(ti, Wcum[i])

    plt.savefig('media/paths.png')
    plt.close()