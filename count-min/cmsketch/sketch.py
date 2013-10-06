
class Sketch:
    """Count-min sketch summary of data"""
    def __init__(self, hashes, width):
        assert len(hashes) >= 1
        assert width > 0

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
