# Calculator Package

## Table of Contents
* Usage
* Methods within the package
* Dependencies
* How to install the package.
  
## Purpose

The purpose of this package is to provide capabilities of mathematical capabilities such as summing, subtracting, multiplying, dividing & taking multiple roots 
from float variables. The package provides ability for verbose action explanation for easier understanding of the operations made and remembers the result of the previous operations.

## Usage

In order to be able to use the package, you first need to install it through (Expanded on later). In order to us the calculator, you first need to instantiate an object from the imported Calculator class. 
The starting arguments of the package are as follows: 

Calculator(0: starting value which all further operations will be done on(default value = 0), False | True: verbose or simple return type - verbose explains what your operation did, whereas simple only returns the answer (default value = False)). 

All further operations are done through methods created within the Calculator class. 

# Methods within the package
* add(*args) - adds sum of all arguments to the value in memory.
   Examples:
   ```
        Calculator(1).add(0.4444, 0.222, 0, 5.55555)
        >>> 7.22195
        Calculator(-100).add(-0.43, -0.2, 5000, 6.0001)
        >>> 4905.3701
        Calculator(-100, True).add(2, 1, 5000, 13444)
        >>> 'You have added 18447 to -100 to get: 18347.'
   ```
* subtract(*args) - subtracts sum of all arguments from the value in memory.
   Examples:
        Calculator(1).subtract(0.4444, 0.222, 0, 5.55555)
        >>> -5.22195
        Calculator(-100).subtract(-0.43, -0.2, 5000, 6.0001)
        >>> -5105.3701
        Calculator(-100, True).subtract(2, 1, 5000, 13444)
        >>> 'You have subtracted 18447 from -100 to get: -18547.'
* multiply(*args) - multiplies the value in memory with all arguments.
   Examples:
   Calculator(1).multiply(0.4444, 0.222, 0, 5.55555)
   >>> 0.0
   Calculator(-100).multiply(-0.43, -0.2, 5000, 6.0001)
   >>> -258004.3
   Calculator(-100, True).multiply(2, 1, 5.001, 13)
   >>> 'You have timed 130.026 with -100.000 to get: -13002.600'
* divide(*args) - divides the value in memory by all arguments.
   Examples:
        Calculator(1).divide(0.4444, 0.222, 2, 5.55555)
        >>> 0.91225
        Calculator(-100).divide(-0.43, -0.2, 5000, 6.0001)
        >>> -0.0388
        Calculator(-100, True).divide(2, 1, 5.001)
        >>> 'You have divided -100.000 by 0.09998000399920015 to get: -9.998.'
* floor_divide(*args) - performs floor division on the value in memory by all arguments.
   Examples:
        Calculator(1).floor_divide(0.4444, 0.222, 0, 5.55555)
        >>> AssertionError: In order to be able to dive the resultin memory with a number,
                                that number must be non-zero.
        Calculator(5).floor_divide(1, 0.2325, 2, 6.2335)
        >>> 1.0
        Calculator(-100).floor_divide(-0.43, -0.2, 5000, 6.0001)
        >>> -1.0
        Calculator(-100, True).floor_divide(2, 4)
        >>> 'You have floor divided -100 by 0.13 to get: -13.'
* root(*args) - returns the result of subsequent root operations on the value in memory by all arguments.
   Examples:
        Calculator(1).root(0.4444, 0.222, 0, 5.55555)
        >>> AssertionError: In order to be able to take a root of a number, 
                        the root number has to be no zero.
        Calculator(5).root(1, 0.2325, 2, 6.2335)
        >>> 1.7424
        Calculator(-100).root(-0.43, -0.2, 5000, 6.0001)
        >>> AssertionError: In order to be able to take a root of a number, it must be non-negative.
        Calculator(1100, True).root(2, 4)
        >>> 'You have taken 2 consecutive roots of 1100 with the root numbers being 2, 4 to get: 2.'
* reset() - resets the value in memory & operation counter.
* change_return_type() - changes the way that the return is given by methods to a verbose/simple type.
  
## Dependencies
Here are the packages used within the package:
* from typing, module Optional.
* from math, module fsum.
* from numpy, module format_float_positional.

## How to install the package

You can install the package in multiple ways: 
1. First of them is to clone the repository and install it through pip from your local directory.

   pip install your/directory/to/the/downloaded/repository/file

2. Second is to install the package directly from the git repository:

   pip install git+https://github.com/repository_directory_on_git.git
  
3. Unfortunately, due to the computer I a was writing from disallowing SSL authentication, the you can not install the package from Test PyPI.
