from functools import update_wrapper
from math import sqrt

class Welford:
    def __init__(self, f):
        self.f = f
        update_wrapper(self, f)
        self.mean = 0
        self.v = 0
        self.trials = 0

    def __call__(self, *args, **kwargs):
        r = self.f(*args, **kwargs)
        self.trials += 1
        d = r - self.mean
        self.v += d**2 * (self.trials - 1)/self.trials
        self.mean += d/self.trials
        return r

    @property
    def stdev(self):
        return sqrt(self.v/self.trials) if self.trials else 0
