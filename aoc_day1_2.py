# aoc_day1_2.py

import sys
import os
from math import floor
from lib.support import load_input

def compute_fuel(mass):
    fuel = floor(int(mass)/3) - 2
    return fuel

def compute_fuel_fuel(fuel_in):
    fuel_out = 0
    fuel_append = 1 # Initialize to 1 to enter while statement...
    iter_count = 1
    while(fuel_append > 0):
        # Compute Fuel Needed to Account for Added Fuel
        fuel_append = compute_fuel(fuel_in)
        
        # Catch when computeted fuel is less then zero
        if(fuel_append <0):
            break
        #print("Iter Count " + str(iter_count) + ": " + str(fuel_append))

        # Compute Iterative Fuel Total And Loop...
        fuel_out = fuel_out + fuel_append
        fuel_in = fuel_append
        iter_count += 1
    
    return fuel_out

# Load Module Mass Elements
input_data = load_input("input_day1.txt")
input_data = input_data.splitlines()

# Iteratively Compute Fuel for Each Module
total_mass = 0
for idx in input_data:
    # Compute Fuel for Module Mass
    mass_fuel = compute_fuel(idx)
    #print("Mass Fuel: " + str(mass_fuel))

    # Compute Appropriate Fuel for Fuel Loaded
    fuel_fuel = compute_fuel_fuel(mass_fuel)
    #print("Fuel Fuel: " + str(fuel_fuel))

    # Sum Resultant Fuels into Total Mass
    total_mass = total_mass + mass_fuel + fuel_fuel

print(total_mass)
