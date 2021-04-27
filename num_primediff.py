import matplotlib.pyplot as plt
from util import *

if __name__ == "__main__":
    x = []
    y = []
    xt = []
    yt = []
    r = 100

    for i in range(r):
        s = sum(prime_divisors(i))
        diff = s - i
        x.append(i)
        y.append(diff)
        if i%1000 == 0: print(i)
    
    plt.plot(x, y)

    for i in range(r):
        s = sum(divisors(i))
        diff = s - i
        xt.append(i)
        yt.append(diff)
        if i%1000 == 0: print(i)

    plt.plot(xt, yt, 'r')
    
    plt.show()
    