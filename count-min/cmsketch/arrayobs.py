
class ArrayObs(object):
    def __init__(self, elements):
        self.counters = [0 for _ in xrange(elements)]

    def obs(self, n):
        self.counters[n] += 1
    
    def count_obs(self, n):
        return self.counters[n]
 
        