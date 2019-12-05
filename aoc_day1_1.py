# aoc_day1_1.py

import sys
import os
from math import floor
from lib.support import load_input

def compute_fuel(mass):
    fuel = floor(int(mass)/3) - 2
    return fuel

# Load Module Mass Elements
input_data = load_input("input_day1.txt")
input_data = input_data.splitlines()

# Iteratively Compute Fuel for Each Module
total_mass = 0
for idx in input_data:
    total_mass = total_mass + compute_fuel(idx)

print(total_mass)
