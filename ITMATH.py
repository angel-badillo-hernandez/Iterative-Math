from typing import Final

# Declaring a constant `PI` of type `float` with a value of `3.141592653589793`.
PI: Final[float] = 3.141592653589793

# Declaring a constant `e` of type `float` with a value of `2.718281828459045`.
e: Final[float] = 2.718281828459045


def capitalSigma() -> str:
    """
    Capital Sigma
    :return: The string '∑'
    """
    return '∑'


def capitalPi() -> str:
    """
    Capital Pi
    :return: The string 'Π'
    """
    return 'Π'


def exp(x: int) -> float:
    """
    Compute the exponential of x

    :param x: the exponent
    :type x: int
    :return: The value of e to the power of x.
    """
    result: float = 1
    for i in range(1, x+1):
        result *= e
    return result


def pow(a: float, x: int) -> float:
    """
    Compute the result of the base a, to the power of x.

    :param a: the base of the power
    :type a: float
    :param x: the exponent
    :type x: int
    :return: The value of a to the power of x.
    """
    result: float = 1
    for i in range(1, x+1):
        result *= a
    return result


def factorial(x: int) -> int:
    """
    Given an integer x, return the factorial of x

    :param x: The number to calculate the factorial of.
    :type x: int
    :return: The factorial of x.
    """
    product: int = 1
    for i in range(1, x+1):
        product *= i
    return product


def combinations(n: int, r: int) -> int:
    """
    The number of ways to choose a sample of r elements from a set of n distinct 
    objects where order does not matter and replacements are not allowed.

    :param n: the number of items in the list
    :type n: int
    :param r: The number of elements to choose from n: The total number of elements
    :type r: int
    :return: The number of combinations of n objects taken r at a time.
    """
    return factorial(n) // (factorial(n-r) * factorial(r))


def permutations(n: int, r: int) -> int:
    """
    Given a number n, return the number of ways to permute n objects
    
    :param n: the number of items in the list
    :type n: int
    :param r: The number of elements to choose from n: The total number of elements
    :type r: int
    :return: The number of permutations of n objects taken r at a time.
    """
    return factorial(n) // factorial(n-r)


def summation(a: int, i: int, n: int) -> int:
    """
    Given an integer a, return the sum of a from i to n
    
    :param a: the first number in the summation
    :type a: int
    :param i: the starting index of the summation
    :type i: int
    :param n: The number of terms to be summed
    :type n: int
    :return: The sum of the first n integers.
    """
    return (n-i+1)*a # Closed form solution

    # Iterative solution below
    # sum: int = a
    # for i in range(i,n):
    #     sum +=a
    # return sum