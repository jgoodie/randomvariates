"""
Author: John Paul Goodman
Course: ISyE 6644
Semester: Fall 2021
Project Group: 40
"""

import numpy as np
from datetime import datetime


class RandomVariates:
    """
    Class method to generate random variates
    """

    def __init__(self):
        self.seed = None
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
        n_fact = np.math.factorial(n)
        k_fact = np.math.factorial(k)
        nk_fact = np.math.factorial(n - k)
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
        Generate a random seed if seed value is None. This helps with randomly generating values.
        :return: a seed value
        """
        if self.seed is None:
            self.seed0 = self.randseed()
            seed = (self.m + self.seed0) % self.m31
        else:
            seed = ((self.m + self.seed0 + self.seed) % self.m31) ** np.pi
        return seed

    def uniform(self, n=1, a=0, b=1):
        """
        Generate uniform random variates
        :param n: number of uniform RVs to generate
        :param a: starting point of uniform range
        :param b: ending point of uniform range
        :return: a numpy array of uniform RVs
        """
        unifs = [self.generateseed()]  # type: list[int]
        for i in range(1, n + 1):
            xi = (self.m * unifs[i - 1]) % self.m31
            unifs.append(xi)
        # simple list append is faster than numpy.append()
        # numpy.append() is shockingly slow. this is because it does a full copy?
        return np.array([(((x * (b - a)) / self.m31) + a) for x in unifs][1:])

    def norm(self, mu=0, sd=1, n=1):
        """
        Generate Normal Random Variates
        :param mu: mean
        :param sd: standard deviation
        :param n: number of random normals to generate
        :return: a numpy array of random normals
        """
        u1 = self.uniform(n=n)
        if self.seed is not None:
            self.seed += 2 ** 34 - 1  # Hack to make sure U1 and U2 look independent
        u2 = self.uniform(n=n)
        theta = 2 * np.pi * u2
        r = np.sqrt(-2 * np.log(u1))
        x = r * np.cos(theta)
        z = mu + (x * sd)
        return z

    def exponential(self, lam=1, n=1):
        """
        Generate Exponential Random Variates
        :param lam: lamba or rate
        :param n: the number of random variates to generate
        :return: a numpy array of random exponentials
        """
        if lam == 0 or lam == 0.0:
            return np.zeros(n)  # zeros for summation
        u1 = self.uniform(n=n)
        exp = (-1 / lam) * np.log(1 - u1)
        return exp

    def erlang(self, lam=1, k=1, n=1):
        """
        Generate Erlang Random Variates
        :param lam: lambda or rate
        :param k: shape parameter
        :param n: number of random variates
        :return: a numpy array of random erlang
        """
        erl = np.ones(n)  # ones for product
        for _ in range(k):
            erl *= self.uniform(n=n)
        erl = (-1 / lam) * np.log(erl)
        return erl

    def weibull(self, lam=1, beta=1, n=1):
        """
        Generate Weibull Random Variates
        :param lam: lambda aka the scale
        :param beta: beta aka the shape
        :param n: number of random variates to generate
        :return: a numpy array of random weibull variates
        """
        return (1 / lam) * (-1 * np.log((1 - self.uniform(n=n)))) ** (1 / beta)

    def triangular(self, a=0, b=1, c=2, n=1):
        """
        Generate Triangular Random Variates
        :param a: lower limit of the triangle
        :param b: mode or peak of the triangle
        :param c: upper limit of the triangle
        :param n: number of triangle random variates
        :return: a numpy array of random triangle variates
        """
        f_c = (b - a) / (c - a)
        u = self.uniform(n=n)
        x_tris = []
        for ui in u:
            if ui <= f_c:
                xi = a + np.sqrt(ui * ((b - a) * (c - a)))
                x_tris.append(xi)
            else:
                xi = c - np.sqrt((1.0 - ui) * ((c - b) * (c - a)))
                x_tris.append(xi)
        return np.array(x_tris)

    def gamma(self):
        pass
