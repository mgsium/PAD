import matplotlib.pyplot as plt
import numpy as np
from util import *

if __name__ == "__main__":
    x = []
    y = []
    r = 10000

    for i in range(r):
        s = sum(divisors(i))
        diff = s - i
        if (abs(diff) < 10):
            x.append(i)
            y.append(diff)
        if i%1000 == 0: print(i)
    
    plt.plot(x, y, "r.")

    # y = x + 1
    xt = np.array(range(0, r))
    yt = [1 for i in range(0, r)]
    plt.plot(xt, yt, 'g.')

    # y = x - 1
    xp = np.array(range(0, r))
    yp = [-1 for i in range(0, r)]
    plt.plot(yp, yp, 'b.')

    plt.show()