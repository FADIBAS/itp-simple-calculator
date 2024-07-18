

# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    # Check if denominator is zero to avoid division by zero
    if y == 0:
        return "Invalid value for denominator, can't divide by 0!"
    return x / y

# Function for squaring a number
def square(x):
    return x ** 2

# Function for raising x to the power of y
def power(x, y):
    return x ** y

# Function for square root
def square_root(x):
    return x ** 0.5
