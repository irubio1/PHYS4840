import numpy as np
import datetime, time
print("location 1")

time.sleep(3) ###hover for 3 seconds
print("location 2")

A = [1,2,3]
print("A: ", A/0)


#(simulations) irubio@RubilYio:~/PHYS4840_labs$ python error2.py
#location 1
#location 2
#Traceback (most recent call last):
  #File "/home/irubio/PHYS4840_labs/error2.py", line 9, in <module>
    #print("A: ", A/0)
                 ~^~
#TypeError: unsupported operand type(s) for /: 'list' and 'int'


## Evaluates syntax error first and THEN logical errors, we're wrong with syntax(the type) already so it doesn't get to 
#the logical error yet