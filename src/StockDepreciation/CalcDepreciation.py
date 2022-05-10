'''
Created on Apr 26, 2022

@author: admin
'''
import math
bvalue = float(input("Enter book value - "))
deprate = float(input("Enter Depreciated  Rate - "))
year = float(input("Enter life of item - "))

finalValue = bvalue*math.pow((1-deprate/100),year)

print("---------------------")
print("Book value is - ",bvalue)
print("Depreciated value is - ",finalValue)