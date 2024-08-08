# program to test path coverage
# Blessing Hlongwane
# HLNBLE002
# 20 April 2023

"""
>>> from palindrome import is_palindrome
>>> print(is_palindrome('a'))
True
>>> print(is_palindrome('ab'))
False
>>> print(is_palindrome('212'))
True
>>> print(is_palindrome('racecar'))
True
>>> print(is_palindrome(""))
True

"""
import doctest
doctest.testmod(verbose=True)