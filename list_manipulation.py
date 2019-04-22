# import numpy as np

# if _name_ == "_main_";
misc_list = ['orange', 'banana', 10, 'leaf', 77.09, 'tree', 'cat']
print('List Length: ', len(misc_list), 'items')
print('Cat Count: ', misc_list.count('cat'), ', Cat Index: ', misc_list.index('cat'))


# Create a list and add to it
temperatures = []
temperatures.append(98.6)
temperatures.append(99.4)	
print(temperatures)		#[98.6, 99.4]


# Extend a list with another list
er_temps = [102.2, 101.1, 99.9]
temperatures.extend(er_temps)	#Extend the list with er_temps
print(temperatures)

# Concatenate two lists
primary_care_doctors = ["Dr. Scholls", "Dr. Pepper"]
er_doctors = ["Doug", "Susan"]
all_doctors = primary_care_doctors + er_doctors 	#concatenate two lists
print(all_doctors)