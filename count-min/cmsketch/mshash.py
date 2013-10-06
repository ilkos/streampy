from random import getrandbits
from math import log

class MultiplyShift(object):
    """h(x) = log2(sz) MSBits [(odd * x) % 2^w]"""
    w = 31
    mask = (1 << w) - 1

    def __init__(self, sz):
        assert sz & (sz - 1) == 0
        self.odd = (getrandbits(self.w - 1) << 1) | 1
        self.width_bits = int(log(sz, 2))
        self.b = getrandbits(self.w - self.width_bits - 1)

    def apply(self, x):
        return ((self.odd * x + self.b) & self.mask) >> (self.w - self.width_bits)
