# Introduction
RandomVariates is a library of random variate generation routines.
The purpose behind this library was purely for educational purposes as 
a way to learn how to generate random variates using such methods as 
inverse transform, convolution, acceptance-rejection and composition 
methods. Additionally, this project was an excuse to get familiar with 
random number generators such as linear congruential generators, 
Tausworthe Generators and Widynski's "Squares: A Fast Counter-Based RNG"

## Pseudo Random Number Generators
The following pseudo random number (PRN) generators are contained in this project:
* A basic "desert island" linear congruential (implemented in the uniform function)
* taus() and tausunif(): A basic Tausworthe PRN generator and a Tausworthe Uniform 
PRN generator
* squaresrng(): Widynski's "Squares: A Fast Counter-Based RNG" 
https://arxiv.org/pdf/2004.06278.pdf 

### Various helper functions to take advantage of the PRN generators
* randseed(): Helper function to grab a "smaller" PRN from the Widynski squares PRN 
generator
* generateseed(): Helper function to generate random seeds if the initial seed has 
not been set
* set_seed() and get_seed(): Functions to get and set the seed.
* reverse(): Helper function to reverse an integer 

## Random Variate Generation Routines
* uniform(): Routine to generate uniform random variates between a and b. 
Default uniform(a=0, b=1)
* norm(): Method to generate random normals. Default norm(mu=0, sd=1)
* exponential(): Generate exponential random variates. 
Default exponential(lam=1)
* erlang(): Routine to generate Erlang_k(lambda) random variates. 
Default erlang(lam=1, k=1, n=1)
* weibull(): Method to generate weibull random variates: Default 
weibull(lam=1, beta=1)
* triangular() Generate triangular random variates with a-lower, b-mode 
and c-upper Default triangular(a=0, b=1, c=2)
* Bernoulli(p) random variates Default bernoulli(p=0.5)
* Routine to generate binomial random variates Default binomial(t=1, p=0.5)
* dicetoss() Simple/fun method to generate X-sides dice toss. Default is 
a simple 6-sided dicetoss(sides=6)
* geometric() Method to generate geometric random variates 
Default geometric(p=0.5)
* negbin() Routine to generate discrete random negative binomials 
Default negbin(t=1, p=0.5)
* chisq() Generate Chi-squared random variates Default chisq(df=1)
* poisson() Method to generate Poisson random variates Default poisson(lam=1)
* gamma() Gamma random variates shape parameter k and a scale parameter θ. 
Implementation is based on Marsaglia and Tsang's transformation-rejection method
of generating gamma random variates 
(https://dl.acm.org/doi/10.1145/358407.358414) Default gamma(k=1.0, theta=1)
* lognormal() Generate lognormal random variates Default lognormal(mu=0, sd=1)
* beta() Routine to generate beta random variates Default beta(a=1, b=1)

## Limitations
* Unlike Numpy's random variate generation routines, these are written
in python. Numpy's routines are written in C hence are much, much faster.
* Beta and Gamma distributions only accept a, b, k and theta greater than one. 
Other random variate implementations, such as Numpy can handle values between
0 and 1.
* Setting the seed does not affect the Tausworthe and Tausworthe Uniform PRN 
generators

### Distributions not currently implemented
* Pearson Type V
* Pearson Type VI
* Log-Logistic
* Johnson Bounded and Johnson unbounded
* Bézier

## Installation
### Requirements:
* Python 3.x
* pip (https://pip.pypa.io/en/stable/installation/)

To install the library, simply run the command:
* pip install randvars

## Usage
To use the library, you need to import the library into your python script then 
create an instance of random variates:
> import randomvariates

> rv = randomvariates.random.RandomVariates()

Alternately you can import random from randomvariates:
> from randomvariates import random

> rv = random.RandomVariates()

### Seeds
By default, a seed is not set when an instance or randomvariates is called.
When a seed is set to None, randomvariates will randomly generate values for the
various random variate routines. For repeatability, we can set a seed by calling 
the set_seed() method. Once a seed has been set, we can verify by calling the 
get_seed() method.

> from randomvariates import random
>
> rv = random.RandomVariates()
> 
> rv.set_seed(42)
>
> rv.get_seed()
> 
> 42

### Pseudo Random Number Generators
To call the Widynski Squares PRN we can call the squaresrng() method. 
The squaresrng() method takes a center and key value. By default, the center
and key are set to 1: squaresrng(ctr=1, key=1)
> rv.squaresrng(42,21)
> 
> 22904061750312427071608663841693658494663185320788517623007713567980053732104718807902410691731255108163475339984462249791973853173096390867949739437289512015166556428304384

As of 11-06-2021, the Tausworthe PRN  and Tausworthe Uniform PRN generator does 
not take a seed value (See Limitations above)
To call the Tausworthe generators, simply call rv.taus() and rv.tausunif(). 
By default taus() will generate 100 binary PRNs and rv.tausunif() will generate 
a single uniform(0,1):

>rv.taus(n=100)
> 
> array([0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
       1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1,
       0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1,
       0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
       0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0])

> rv.tausunif(n=1)
> 
>array([0.22627192])

**Linear Congruential Generator (LCG)**

The Uniform PRN generator is based off a "desert island" LCG of the form:

> X_{i} = 16807 X_{i-1} mod(2**32 - 1)

To call the uniform PRN generator simply call:
> rv.uniform()
> 
> array([0.0028378])

To generate more than one unif(0,1), call the method with n=X where X is the number 
of unif(0,1)s to generate:

> rv.uniform(n=25)
> 
> array([0.0028378 , 0.69495865, 0.17008364, 0.59578035, 0.28035944,
       0.00113405, 0.05993272, 0.28927888, 0.91019703, 0.68147951,
       0.62609725, 0.81650574, 0.01200872, 0.83049583, 0.14336138,
       0.4747437 , 0.01741077, 0.62288295, 0.79372406, 0.12022883,
       0.68598241, 0.3064384 , 0.31021374, 0.76239295, 0.53823463])

If we want to generate something other than unif(0,1), we can call the function
with a=X and b=Y where X and Y are the lower and upper bounds of the uniform 
distribution:

> rv.uniform(a=7, b=11, n=25)
> 
> array([ 7.01135121,  9.77983461,  7.68033457,  9.3831214 ,  8.12143777,
        7.00453619,  7.23973089,  8.15711553, 10.64078812,  9.72591803,
        9.50438901, 10.26602297,  7.04803487, 10.32198331,  7.57344553,
        8.89897481,  7.0696431 ,  9.4915318 , 10.17489623,  7.48091533,
        9.74392966,  8.22575361,  8.24085498, 10.04957178,  9.15293853])

### Distributions
**Normal Random Variates**

To generate random normal random variates, call the norm() function. By default, 
the norm() function will generate values with mean = 0 and standard deviation = 1.

> rv.norm(n=25)
> 
> array([-1.33438863,  0.12180611,  0.88656523,  0.50965537, -1.64358406,
       -0.25778164,  0.57095618,  1.90310886, -0.05967737, -0.34183211,
        1.40942348,  0.588753  , -2.00879407, -0.27557057, -0.05367554,
        0.36562436,  1.51957859, -0.87597507,  0.27341912,  0.99870143,
        0.0563413 , -0.58931763,  0.06256761,  1.34552544, -0.41456673])

To generate normals with other means and standard deviations, simply specify them 
when calling the function:

> rv.norm(mu=42, sd=21, n=25)
> 
> array([31.09197496, 90.91916642, 10.96438887, 63.22805106, 11.65331438,
       42.3934924 , 31.50241102, 57.32494887, 39.63622134, 50.84789244,
       29.66813461, 71.59768198, 51.23679519, 29.62926174, 38.93133399,
       21.33704934, 44.01056639, 85.43369206, 10.93161744, 35.5352881 ,
       47.6567116 , 62.89812129, 35.67247842, 48.76775665, 37.78179072])

**Exponential Random Variates**

By default, the exponential() functin will generate a single, lambda=1 random variate.

> rv.exponential()
> 
> array([1.11685025])

To generate exponentials with different rates (lambda), call the exponential function
with lam=X, where X is 1/X rate:

> rv.exponential(lam=42, n=25)
> 
> array([0.02659167, 0.05889761, 0.0237974 , 0.05500891, 0.00990581,
       0.00665694, 0.01027128, 0.00311863, 0.00991187, 0.00155661,
       0.02532011, 0.00358105, 0.06095103, 0.02608557, 0.03126096,
       0.01844892, 0.04179501, 0.00204212, 0.01357267, 0.02956585,
       0.05493093, 0.04847486, 0.03083947, 0.03648715, 0.02353137])

**Erlang Random Variates**

Random Erlang variates can be generated by calling the erlang() function. By default,
the erlang function will generate variates with lambda = 1 and shape (k) = 1:

> rv.erlang()
> 
> array([0.39646936])

To generate erlangs with different rate and shape parameters, set lam=X and k = Y,
where X is the lambda rate and Y is the shape:

> rv.erlang(lam=5, k=5, n=25)
> 
> array([0.39646936, 0.08803646, 0.45897164, 0.10449879, 1.07778402,
       1.41096694, 1.04868842, 2.09746919, 1.07729126, 2.76008462,
       0.42352393, 1.96869049, 0.08046101, 0.40697774, 0.31337257,
       0.61761435, 0.18975684, 2.49867301, 0.8335498 , 0.34090517,
       0.10486022, 0.13990266, 0.31996746, 0.24335083, 0.46553741])

**Weibull Random Variates**

To generate values from the Weibull distribution, call the weibull() method with 
lam and beta. By default, lam and beta are set to 1 weibull(self, lam=1, beta=1).

> rv.weibull()
> 
> array([0.00284184])

To generate weibull values with different lam (shape) and beta (scale), set lam 
and beta as such:

> rv.weibull(lam=3, beta=5, n=25)
> 
> array([0.10318073, 0.34497802, 0.23822211, 0.32680215, 0.26688172,
       0.08587253, 0.19102132, 0.26887509, 0.39745421, 0.3424279 ,
       0.33224353, 0.37046057, 0.13781682, 0.37386295, 0.2295085 ,
       0.30523775, 0.14852653, 0.33166333, 0.36519926, 0.22099585,
       0.34327599, 0.2726182 , 0.2734267 , 0.35840856, 0.31657801])

**Triangular Random Variates**

By default, the randomvariates library will generate Triangular(0,1,2) values from 
a triangular distribution:

> rv.triangular()
> 
>array([0.07533662])

To generate values from a Triangular distribution with lower bound a, mode b and 
upper bound c, call the triangular() function with a, b, and c set:

> rv.triangular(a=-5, b=0, c=5, n=25)
> 
> array([-4.6233169 ,  1.09461047, -2.08380691,  0.50433737, -1.25594176,
       -4.76187742, -3.26892052, -1.19685075,  2.88100295,  1.00925764,
        0.67621261,  1.97102115, -4.22512206,  2.08877884, -2.32267501,
       -0.12791778, -4.06697336,  0.65766738,  1.7884899 , -2.54817586,
        1.0375665 , -1.08567757, -1.06163902,  1.55321124,  0.19497467])

**Bernoulli Random Variates**

To generate bernoulli(p) random values, call the bernoulli() method with 
probability, p. By default, the bernoulli() method generates bernoulli(0.5) random
values.

> rv.bernoulli()
> 
> array([0])
> 
> rv.bernoulli(n=25)
> 
>array([0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0,
       0, 1, 1])

To generate bernoulli(0.8) random values, set p=0.8:

> rv.bernoulli(p=0.8, n=25)
> 
> array([0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1,
       1, 1, 1])

**Binomial Random Variates**

Binomial(n,p) random values can be generated with the binomial() function.
By default, the binomial() function generates 1 trial at p=0.5:

> rv.binomial()
> 
> array([0])

Note: Don't confuse t=trials and n=number of values to generate. To generate 25 
binomials with 10 trials, and probability 0.5, we would specify 
binomial(t=10, p=0.5, n=25): 

> rv.binomial(t=10, p=0.5, n=25)
> 
> array([6, 5, 3, 3, 5, 3, 5, 7, 6, 5, 3, 5, 4, 5, 4, 4, 2, 6, 6, 6, 4, 4,
       6, 5, 2])

**Random X-sided Dice Toss**

For the D&D fans, the dicetoss() function allows you to generate an X-sided
die toss. For example, to generate 10, 20-sided dice tosses, simply call the 
dicetoss() function. By default, dicetoss() defaults to a 6-sided die:

> rv.dicetoss(n=10)
> 
> array([6., 6., 5., 1., 6., 3., 1., 5., 3., 5.])

To generate 10, 20-sided dice toss, set the side variable to 20:

>rv.dicetoss(sides=20, n=10)
> 
> 
> array([20., 20., 17.,  4., 20., 10.,  3., 15., 10., 14.])

**Geometric Random Variates**

To generate geometric random values, use the geometric() function. By default, 
the geometric function is set to a probability of 0.5:

> rv.geometric()
> 
> array([5.])

To generate geometric values with a different probability, set p equal to the new 
probability:

> rv.geometric(p=0.42, n=25)
> 
> array([ 7., 12.,  4.,  1.,  6.,  2.,  1.,  3.,  2.,  3.,  1.,  1.,  2.,
        1.,  2.,  7.,  3.,  1.,  4.,  2.,  1.,  2.,  2.,  4.,  1.])

**Negative Binomial Random Variates**

To generate negative binomial random variates, call the negbin() funtion. By default.
negbin() will generate values with a probability of 0.5 and 1 trial:

> rv.negbin()
> 
> array([1.])

To generate 25 negbin values with a probability of 0.42 and 10 trials:

> rv.negbin(t=10, p=0.42, n=25)
> 
> array([35., 21., 30., 26., 24., 24., 20., 28., 21., 22., 29., 18., 22.,
       26., 19., 19., 22., 22., 21., 25., 25., 26., 22., 27., 24.])

**Chi-Squared Random Variates**

Chi-Squared random values can be generated by calling the chisq() method.
By default, chisq() generates values with df=1:

> rv.chisq()
> 
> array([0.02609475])

