from random import lognormvariate
from cmsketch import sketch, rangequery
from collections import defaultdict
import matplotlib.pyplot as plt

if __name__ == "__main__":
    nums = [int(lognormvariate(1, 0.6) * 1000) for i in range(1000000)]

    sketch = sketch.Sketch.fromParameters(10**-4, 0.0002)
    rangeq = rangequery.RangeQuery(200000)

    d = defaultdict(int)
    for num in nums:
        sketch.obs(num)
        rangeq.obs(num)
        d[num] += 1

    x = sorted(d.iterkeys())
    y = []
    newy = []
    realsums = []
    estsums = []
    sum = 0
    for key in x:
        y.append(d[key])
        sum += d[key]
        realsums.append(sum)
        estsums.append(rangeq.subset(0, key))
        obs = sketch.count_obs(key)
        newy.append(obs)

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(x, y, color = 'red')
    
    ax2 = fig.add_subplot(212)
    ax2.plot(x, newy, color = 'green')
    plt.legend()
    plt.show()

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(x, realsums, color = 'red')
    
    ax2 = fig.add_subplot(212)
    ax2.plot(x, estsums, color = 'green')
    plt.legend()
    plt.show()