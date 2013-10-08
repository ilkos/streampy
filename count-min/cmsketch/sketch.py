import mshash
import math

class Sketch(object):
    """ Count-min sketch summary of data
    Estimate upper bounded by e(x) <= f(x) + eps * num_distinct(input) with probability 1 - delta
    Where e(x) estimate count, f(x) actual count
    """
    @classmethod
    def fromParameters(cls, delta, epsilon):
        width = int(math.ceil(math.exp(1) / epsilon))
        rnd_width = int(pow(2, math.ceil(math.log(width, 2))))
        depth = int(math.ceil(math.log(1 / delta)))
        return cls([mshash.MultiplyShift(rnd_width) for _ in xrange(depth)], rnd_width)

    def __init__(self, hashes, width):
        assert len(hashes) >= 1
        assert width > 0
        
        print("Using %d hashes, width: %d - total size: %d" % (len(hashes), width, len(hashes) * width))
        self.hashes = hashes
        self.width = width

        self.counters = [[0] * self.width for _ in xrange(len(self.hashes))]
        self.observed = 0

    def obs(self, num):
        self.observed += 1
        for i in xrange(len(self.hashes)):
            self.counters[i][self.hashes[i].apply(num) % self.width] += 1

    def count_obs(self, num):
        return min(self.counters[i][self.hashes[i].apply(num) % self.width] for i in xrange(len(self.hashes)))
