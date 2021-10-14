"""
Author: John Paul Goodman
Course: ISyE 6644
Semester: Fall 2021
Project Group: 40
"""

import math
from datetime import datetime


class RandomVariates:
    """
    Class method to generate random variates
    """
    def __init__(self):
        self.seed = 0  # Fix this so that init is None, then fix things so that we can have a seed of 0
        self.prn = 0
        self.seed0 = 2 ** 23 - 1
        self.m = 16807
        self.m31 = (2 ** 31 - 1)

    @staticmethod
    def nchoosek(n, k):
        """
        n choose k
        :param n:
        :param k:
        :return:
        """
        n_fact = math.factorial(n)
        k_fact = math.factorial(k)
        nk_fact = math.factorial(n - k)
        res = n_fact / (k_fact * nk_fact)
        return res

    @staticmethod
    def reverse(n=0):
        """
        reverses an integer
        :return: reversed integer
        """
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n = n // 10
        return rev

    @staticmethod
    def squaresrng(ctr, key):
        """
        B. Widynski
        https://arxiv.org/pdf/2004.06278.pdf
        :param ctr: the center
        :param key: the key
        :return: very large random number
        """
        y = x = ctr * key
        z = y + key
        x = x * x + y
        x = (x >> 32) | (x << 32)  # round 1
        x = x * x + z
        x = (x >> 32) | (x << 32)  # round 2
        x = x * x + y
        x = (x >> 32) | (x << 32)  # round 3
        return (x * x + z) >> 32  # round 4

    def randseed(self):
        """
        Get random number from square
        :return: smaller random number
        """
        # int.from_bytes(os.urandom(7), sys.byteorder)
        i = int(datetime.now().timestamp() * 1000000)
        r = self.reverse(int(datetime.now().timestamp() * 1000000))
        self.prn = self.squaresrng(i, r) % 100000000000
        return self.prn

    def set_seed(self, seed):
        """
        Set the seed
        :param seed: seed value
        """
        self.seed = seed

    def get_seed(self):
        """
        Get the seed
        """
        return self.seed

    def generateseed(self):
        """
        Generate a random seed if initial seed value is 0 else
        :return: a seed value
        """
        if self.seed == 0:
            self.seed0 = self.randseed()
            seed = (self.m + self.seed0 + self.seed) % self.m31  # reversed m and m31, self.m * self.seed0
        else:
            seed = ((self.m + self.seed0 + self.seed) % self.m31)**math.pi  # reversed m and m31, self.m * self.seed0
        return seed

    def uniform(self, n=1, a=0, b=1):
        """
        Generate uniform random variates
        :param n: number of uniform RVs to generate
        :param a: starting point of uniform range
        :param b: ending point of uniform range
        :return: an array of uniform RVs
        """
        # if self.seed == 0:
        #     self.seed0 = self.randseed()
        #     seed = (self.m31 * self.seed0 + self.seed) % self.m
        # else:
        #     seed = (self.m31 * self.seed0 + self.seed) % self.m
        # unifs = [seed]  # type: list[int]
        unifs = [self.generateseed()]  # type: list[int]
        for i in range(1, n + 1):
            xi = (self.m * unifs[i - 1]) % self.m31
            unifs.append(xi)
        return [(((x * (b - a)) / self.m31) + a) for x in unifs][1:]  # type: list[float]

    def norm(self, mu=0, sd=1, n=1):
        """
        Generate Normal Random Variates
        :param mu: mean
        :param sd: standard deviation
        :param n: number of random normals to generate
        :return: a list of random normals
        """
        u1 = self.uniform(n=n)
        if self.seed != 0:
            self.seed += 2**34 - 1  # Hack to make sure U1 and U2 are independent
        u2 = self.uniform(n=n)
        theta = [2 * math.pi * u for u in u2]
        r = [math.sqrt(-2 * math.log(u)) for u in u1]
        # x1 = [xi[0] * math.cos(xi[1]) for xi in zip(r, theta)]
        # x2 = [xi[0] * math.sin(xi[1]) for xi in zip(r, theta)]
        x = [xi[0] * math.cos(xi[1]) for xi in zip(r, theta)]
        z = [mu + (xj * sd) for xj in x]
        return z

    def exponential(self, lam=1, n=1):
        U = self.uniform(n=n)
        exp = [-1 * (1 / lam) * math.log(u) for u in U]
        # exp = [-1 * (1 / lam) * math.log(1-u) for u in U]
        return exp

    # Erlang: https://en.wikipedia.org/wiki/Erlang_distribution#Generating_Erlang-distributed_random_variates
