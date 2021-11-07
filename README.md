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
* gamma() Gamma random variates shape parameter k and a scale parameter θ
Default gamma(k=1.0, theta=1)
* lognormal() Generate lognormal random variates Default lognormal(mu=0, sd=1)
* beta() Routine to generate beta random variates Default beta(a=1, b=1)

## Limitations
* Unlike Numpy's random variate generation routines, these are written
in python. Numpy's routines are written in C hence are much, much faster.
* Beta and Gamma distributions only accept a, b, k and theta greater than one. 
Other random variate implementations, such as Numpy can handle values between
0 and 1.

### Distributions not currently implemented
* Pearson Type V
* Pearson Type VI
* Log-Logistic
* Johnson Bounded and Johnson unbounded
* Bézier


