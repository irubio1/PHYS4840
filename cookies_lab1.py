
#Determine amount of money available
max_money = int(input("Enter the amount of money you have for cookies"))
print(type(max_money))


### Define useful quantities

Sugar_price = 2.65
Chocolate_price = 3.20
Snickerdoodle_price = 3.45
Smores_price = 3.70

cookie_names= ["Sugar", "Chocolate", "Snickerdoodle", "Smores"]
cookie_prices = [Sugar_price, Chocolate_price, Snickerdoodle_price, Smores_price]

#Easier challenge
def change_and_cookienumber(variable):
	cookienumber = max_money//variable
	change = round(max_money%(cookienumber*variable), 2)
	print(f"With  {max_money} dollars, we can buy {cookienumber} with {change} dollars left.")



for cookie_price in cookie_prices:
	change_and_cookienumber(cookie_price)
		

#### I realized after looking at Dr. Joyce's solution that I did not include the name of the cookie
### that was being looped over, I tried extracting the name of the variables but that didn't work and
### I took it out 
	
print("-------------------------------------------------------------")



### Actual Solution ###

#!/usr/bin/python3.8
#####################################
#
# Solutions Lab 1 Exercise 2
# Author: M Joyce
#
#####################################


import numpy as np
import sys
max_money = input('enter the amount of money you have for cookies: ')
#max_money = 10.0
max_money = float(max_money)



# Price list:
# Sugar – $2.65
# Chocolate – $3.20
# Snickerdoodle – $3.45
# S’mores – $3.70
sugar_price = 2.65
choc_price = 3.20
snick_price = 3.45
smore_price = 3.70


n_sugar = np.floor(max_money / sugar_price)
#n_sugar_2 = max_money // sugar_price
#print('same? ', n_sugar, n_sugar_2) ## yes
n_choc = np.floor(max_money / choc_price)
n_snick = np.floor(max_money / snick_price)
n_smore = np.floor(max_money / smore_price)
#print(n_sugar, n_choc, n_snick, n_smore)
change_sugar = max_money % sugar_price
change_choc = max_money % choc_price
change_snick = max_money % snick_price
change_smore = max_money % smore_price
change_sugar = round(change_sugar, 2)
change_choc = round(change_choc, 2)
change_snick = round(change_snick, 2)
change_smore = round(change_smore,2)
print('you can have', n_sugar, ' sugar cookies with $',change_sugar, ' in change remaining')
print('you can have', n_choc, ' chocolate cookies with $',change_choc, ' in change remaining')
print('you can have', n_snick, ' snickerdoodles with $',change_snick, ' in change remaining')
print('you can have', n_smore, " s'mores cookies with $",change_smore, ' in change remaining')

###########################################
#
# the array casting below is the core weakness of this solution!
# If the cookie_type and spare_change arrays are not
# ordered in precisely this way, argmin() from one vector
# will not correctly index the other vector
#
###########################################

cookie_type = np.array(['sugar', 'chocolate', 'snickerdoodle', "s'mores"])
spare_change = np.array([change_sugar, change_choc, change_snick, change_smore])
print('minimum spare change: ', spare_change.min())
print('index of the minimum value in the array: ', spare_change.argmin() )
which_cookie = cookie_type[spare_change.argmin()]
print('The single type of cookie that minimizes change is: ', which_cookie)
