# program to test path coverage
# Blessing Hlongwane
# HLNBLE002
# 20 April 2023


"""
>>> from numberutil import aswords
>>> print(aswords(109))
one hundred and nine
>>> print(aswords(133))
one hundred and thirty three
>>> print(aswords(140))
one hundred and forty
>>> print(aswords(60))
sixty
>>> print(aswords(100))
one hundred
>>> print(aswords(0))
zero
>>> print(aswords(10))
ten
>>> print(aswords(26))
twenty six

"""
import doctest
doctest.testmod(verbose=True)