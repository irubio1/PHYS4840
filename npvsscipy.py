#!/usr/bin/python3.8

import numpy as np
from scipy.special import sqrt

my_number = 16

from_numpy = np.sqrt(my_number)
from_scipy = sqrt(my_number)

print("NUMPY: ", from_numpy, " SCIPY: ", from_scipy)



#### (simulations) irubio@RubilYio:~/PHYS4840_labs$ python npvsscipy.py
#Traceback (most recent call last):
#  File "/home/irubio/PHYS4840_labs/npvsscipy.py", line 4, in <module>
#    from scipy.special import sqrt
#ImportError: cannot import name 'sqrt' from 'scipy.special' (/home/irubio/simulations/lib/python3.12/site-packages/scipy/special/__init__.py)