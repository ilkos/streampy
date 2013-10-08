import sketch
import arrayobs
import math

class RangeQuery(object):
    """ Supports subset sum queries in [x, y] in log2(y - x) time """
    def __init__(self, supported_range):
        """Initialises with support for range [0, ceil_pow2(supported_range))"""
        self.supported_range = int(pow(2, math.ceil(math.log(supported_range, 2))))
        self.num_counters = int(math.log(self.supported_range, 2)) + 1
        self.counters = [self.get_counter(pow(2, i)) for i in xrange(self.num_counters)]

    def get_counter(self, size):
        if size <= 16384:
            return arrayobs.ArrayObs(size)
        else:
            return sketch.Sketch.fromParameters(10**-3, 0.001)

    def subset(self, qlo, qhi):
        """Return number of observed elements in [qlo, qhi]"""
        assert qlo >= 0 and qlo < self.supported_range
        assert qhi >= 0 and qhi < self.supported_range
        assert qlo <= qhi
        return self.__traverse(qlo, qhi, 0, self.supported_range - 1, 0, 0)

    def __traverse(self, qlo, qhi, lo, hi, level, idx):
        if (qhi < lo or qlo > hi):
            return 0

        if (qlo <= lo and qhi >= hi):
            print (qlo, qhi, lo, hi, level, idx, self.counters[level].count_obs(idx))
            return self.counters[level].count_obs(idx)

        mid = lo + (hi - lo) / 2
        s = self.__traverse(qlo, qhi, lo, mid, level + 1, 2 * idx) + \
              self.__traverse(qlo, qhi, mid + 1, hi, level + 1, 2 * idx + 1)
        return s

    def obs(self, n):
        """Increments counters through all levels for n"""
        assert n >= 0 and n < self.supported_range
        self.__obs(n, 0, self.supported_range - 1, 0, 0)

    def __obs(self, n, lo, hi, level, idx):
        st = [(lo, hi, level, idx)]
        while st:
            lo, hi, level, idx = st.pop()
            if not (lo <= n <= hi) or lo > hi or level >= self.num_counters:
                return
            self.counters[level].obs(idx)
            mid = lo + (hi - lo) / 2
            st.append((lo, mid, level + 1, 2 * idx))
            st.append((mid + 1, hi, level + 1, 2 * idx + 1))
