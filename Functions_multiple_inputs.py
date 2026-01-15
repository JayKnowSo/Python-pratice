# Functions can take more than one parameter
# Values are passed in the same order as parameters
# This builds reusable logic

def greet(name, time_of_day):
    print(f"Good {time_of_day}, {name}!")

name = input("Enter your name:")
time = input("Enter time of day (mourning/afternoon/evening):")

greet(name, time)