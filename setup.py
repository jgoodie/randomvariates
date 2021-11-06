import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='randvariates',
     version='0.1',
     scripts=['RV.py'],
     author="John Goodman",
     author_email="john.goodman@gmail.com",
     description="A library of random variate generation routines",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/jgoodie/randomvariates",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
