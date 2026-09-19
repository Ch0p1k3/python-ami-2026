import resource


class Vector2d:
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


NUM_VECTORS = 10**6

mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print("Creating {:,} Vector2d instances".format(NUM_VECTORS))

vectors = [Vector2d(3.0, 4.0) for i in range(NUM_VECTORS)]

mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print("Initial RAM usage: {:14,}".format(mem_init))
print("  Final RAM usage: {:14,}".format(mem_final))
