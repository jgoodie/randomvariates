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
* Routine to 

## Limitations
* Unlike Numpy's random variate generation routines, these are written
in python. Numpy's routines are written in C hence are much, much faster.


