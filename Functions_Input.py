# Notes: This combines functions with user input
# Shows how to reuse logic for different users
# Each call uses a different input

def greet(name):
    print(f"What city do you live in? {name}!")

user_name = input("Enter your name:")
greet(user_name)