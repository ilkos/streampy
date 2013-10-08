from cmsketch import rangequery
import unittest

class TestRange(unittest.TestCase):
    def testSimplestRange(self):
        rq = rangequery.RangeQuery(2)
        rq.obs(0)
        self.assertEqual(1, rq.subset(0, 0), "Simple range")
