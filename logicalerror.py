import numpy as np
import datetime, time
print("location 1")

time.sleep(3) ###hover for 3 seconds
print("location 2")

A = 3
print("A: ", A/0)


#(simulations) irubio@RubilYio:~/PHYS4840_labs$ python logicalerror.py
#location 1
#location 2
#Traceback (most recent call last):
  #File "/home/irubio/PHYS4840_labs/logicalerror.py", line 9, in <module>
   #print("A: ", A/0)
                 ~^~
#ZeroDivisionError: division by zero