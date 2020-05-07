import random
import math 
from Crypto.Util.number import long_to_bytes,bytes_to_long

from itertools import product
from string import *
keywords = [''.join(i) for i in product(ascii_lowercase+ascii_uppercase+digits+' ', repeat = 4)]
for i in range(len(keywords)):
 print keywords[i]
