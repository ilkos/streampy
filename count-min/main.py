from random import lognormvariate
from cmsketch import sketch
from collections import defaultdict
import matplotlib.pyplot as plt

if __name__ == "__main__":
    nums = [int(lognormvariate(1, 0.6) * 1000) for i in range(1000000)]

    sketch = sketch.Sketch.fromParameters(10**-4, 0.0002)

    d = defaultdict(int)
    for num in nums:
        sketch.obs(num)
        d[num] += 1

    x = sorted(d.iterkeys())
    y = []
    newy = []
    for key in x:
        y.append(d[key])
        obs = sketch.count_obs(key)
        newy.append(obs)

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(x, y, color = 'red')
    
    ax2 = fig.add_subplot(212)
    ax2.plot(x, newy, color = 'green')
    plt.legend()
    plt.show()
