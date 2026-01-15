# Notes: User input controls loop reptition
# Functions organize repeated logic
# Combines input, loops, and functions

def greet_multiple_times(name, times):
    for i in range(times):
        print(f"Hey are you there? {name}! (loop {i})")

name = input("Enter your name:")
times = int(input("How many times should i ask you?"))

greet_multiple_times(name, times)