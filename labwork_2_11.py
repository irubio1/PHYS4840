#!/usr/bin/python3.12


#Excercise: floating_point precision


print(0.1+0.2)
print(repr(0.1+0.2))

### repr() give a literal respresentation of a variable, gives EXACT value
###16 digits of precision(in practice, 15-17 digits)

#Excercise: subtraction of near equal numbers


from math import sqrt
x = 1.0
y = 1.0 + (1e-14)*sqrt(2)

answer_1 = 1e14*(y-x)
answer_2 = sqrt(1)
percentage_difference = (1-(answer_2/answer_1))*100

print("answer1: ", answer_1)
print("answer2: ", answer_2)
print("Percentage difference: ", percentage_difference)

#Weakness: Memory management and limitations
#Weakness: Random number generation

#TIMING YOUR CODE