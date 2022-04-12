######################################################################
# Program Filename: wind
# Author: Morgan Flesland
# Date: 11 april 2022
# Description: This program will compute the amount of energy made
# from wind turbines of different efficiencies and compare the energy
# output to that of burning coal.
# Input: Turbine efficiency and size and wind speed
# Output: Energy used from turbines
######################################################################
#given
speed=(12.29)
r=(3.0)
efficiency=(0.10)
#equations
a=3.14159265*(r**2)
Pmax=0.5*1.2*a*(speed**3)
Pactual=Pmax*efficiency
#answers
print(Pactual)
print(Pmax)