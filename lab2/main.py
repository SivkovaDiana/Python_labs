from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('X, N, Sum')

N=888888
Sum[X] = ((1+X)*X)/2
print(Sum[N] == Sum)