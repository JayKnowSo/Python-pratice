# Notes: Functions can return formatted strings
# Multiple parameters allow flexible input
# Returned values can be printed or reused
# .upper() for all caps, shows return values can be used further

def greet(name, time_of_day):
    return f"Good {time_of_day}, {name}!"

name = input("Enter your name:")
time = input("Enter time of day (mourning/afternoon/evening):")

message = greet(name, time)
print(message.upper())