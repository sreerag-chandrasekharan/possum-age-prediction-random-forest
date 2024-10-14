import numpy as np
import copy
import math
from scipy.stats import norm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib.ticker import MaxNLocator
dlblue = '#0096ff'; dlorange = '#FF9300'; dldarkred='#C00000'; dlmagenta='#FF40FF'; dlpurple='#7030A0'; 
plt.style.use('./style.mplstyle')

def load_data():
    data = np.loadtxt("possum.txt", delimiter=',', skiprows=1)
    X = data[:,:6]
    y = data[:,6]
    return X, y
