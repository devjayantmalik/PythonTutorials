# ==================================================
# ==================================================
#   Functions as objects, function Annotations,
#   Lambda Anonymous functions, Map, filter,
#   Reduce
# ==================================================
# ==================================================

# Create a function to return num * 2
# Assign the function to a variable
# Now use that variable for function invocation


# =============================================
# Use the above function multiply_by_two as it is
# Create a function math_is_fun() and receive function2 and num1 as its argument
# Now return function2(num1)




# ===============================================
# Return a function from within a function
# and also demonstrate dynamically create a function

# Hints:
# Create a function with argument one
# Create another function2 in body of function1 with argument two
# return function2
# Store the output in generated_function



# =======================================
# Store functions inside of data structures : generated_func, multiply_by_two
# Now access the functions using index


# =================================================
# Create a function that receives a list and a function
# The function passed will return True or False if a list value is odd
# The surrounding function will return a list of odd numbers.




# ==============================================
#           Function Annotations
# =============================================

# Function annotations are used for documentation purposed only.
# These have no impact on behaviour of function


# ================================================
# Create a function world_is_awesome with
# name as string, age as int datatype specified in function
# Also use the function annotation to specify that the function
# returns string
# Demonstrate how to print the annotations of the function



# ==========================================
#           Lambda Functions
# ==========================================

# Lambda functions do not require a name and they are
# also known as anonymous function.

# Syntax:
# lambda arg1, arg2, arg3, arg4:
#       expression or statements


# ======================================
# Create a lambda function to add 3 nums


# ======================================
# Create a lambda function to return true
# if a person can vote and false if he can't
# Use ternary operator to solve this problem



# =============================================
# Create a list of lambda functions to calculate
# different power of numbers taking num as argument.
# Let's say we pass num = 4
# Then we should be able to calculate 4 ** 2, 4 ** 3, 4 ** 4
# Use for loop to execute each function


# =============================================
# Store lambdas inside of dictionary
# Use warrior attack as an example
# Create three keys inside of dictionary: quick, power, miss
# and Quick Attack, Power Attack, Missed Attack using lambda function


# ===============================================
# Create a random list filled with the characters 'H' or 'T'
# for heads and tails
# Output the no of heads and tails
# Ask the user no of times the coin was tossed

# Sample output:
# Enter no of times the coin was tossed: 50
# Heads: 46
# Tails: 54



# =============================================
#               Map
# =============================================

# Map allows us to operate a function on all items of the list.

# ===============================================
# Generate a list of numbers from 1 to 10
# Create a function that returns num * 2
# Use map function to print doubles of the each no in the list


# ==================================
# Use lambda and map to get doubles of above list oneTo10



# ============================================
# Create two lists and use lambda to add
# same element at index of list1 to element at
# same index in list2


# =========================================
# print 3 blank lines using single print statement
print("\n" * 3)


# ==========================================
#           Filter
# ==========================================


# ===========================================
# Use filter and lambda to generate even values from the list
# Use range function to generate a list



# ===================================================
# Find the multiples of 9 from a random 100 value list with
# values between 1 and 1000



# =============================================
#                   Reduce
# =============================================

# To use reduce import it from functools module
# Reduce receives a list and returns a single result


# =============================================
# Add all the values in the list using reduce
# use range function to generate a list
# Use lambda to sum two nos

