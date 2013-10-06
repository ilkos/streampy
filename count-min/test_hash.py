from cmsketch import mshash

def test_distribution(h, iterable, nbuckets):
    buckets = [0] * nbuckets
    items = 0
    for i in iterable:
        buckets[h.apply(i) % nbuckets] += 1
        items += 1

    print ("Max: %d - min %d - average: %f - expected: %d " % (
                max(buckets), min(buckets), sum(buckets) / float(len(buckets)), items / nbuckets))

    import matplotlib.pyplot as plt
    plt.plot(range(nbuckets), buckets)
    plt.show()

if __name__ == "__main__":
    test_distribution(mshash.MultiplyShift(8192), xrange(1, 1000000), 8192)