# num cars in fleet
cars = 100
# seats in a single car
space_in_car = 4
# drivers available
drivers = 30
# passengers who need a ride
passengers = 90
# excess capacity in fleet
cars_not_driven = cars - drivers
# can't drive more cars than we have drivers
cars_driven = drivers
# how many seats in cars we have
carpool_capacity = cars_driven * space_in_car
# transportation efficiency
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

'''
Exercise Notes
1.
'''
