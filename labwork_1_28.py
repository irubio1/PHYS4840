
###Mini excerise

#When I enter 'echo $Shell' into the terminal line I get:
#'/bin/bash' which indicates that my shell is bash


###1. 'which python'
## '/home/irubio/simulations/bin/python'


###2. 'echo PYTHON_PATH'
##'PYTHON_PATH'


###3.'echo $PYTHON_PATH'
##''

###4. 'export PYTHON_PATH=/home/irubio/simulations/bin/python'
###'echo $PYTHON_PATH'
##'/home/irubio/simulations/bin/python'

#(simulations) irubio@RubilYio:~$ ps -p $$
#    PID TTY          TIME CMD
#  17944 pts/0    00:00:00 bash





import numpy as np
import datetime, datetime
print("location 1")

time.sleep(3) ###hover for 3 seconds
print("location 2")

A = np.array([1,2,3]
print("A: ", A)

###When we run this code, we get a syntax error

#(simulations) irubio@RubilYio:~/PHYS4840_labs$ python labwork_1_28.py
# File "/home/irubio/PHYS4840_labs/labwork_1_28.py", line 38
#    A = np.array([1,2,3]
#                ^
#SyntaxError: '(' was never closed


#this labwork includes logicalerror.py, 

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