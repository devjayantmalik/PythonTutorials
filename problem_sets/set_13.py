# ==================================================
# ==================================================
#    Iterabale, Iterator, List Comprehensions,
#   Generator Functions, Generator Expressions
# ==================================================
# ==================================================


# Difference between Iterator and Iterable:
# Iterable:
# It is a series of elements that can be iterated.
# It does not have any iteration state such as, "current element",
# instead it has one method that produces an iterator.
# The object is named __iter__

# Iterator:
# It is an object with iteration state.
# It lets you check if it has more
# elements using hasNext()(in case of java) method
# and move to next element using next() method
# The object is named __next__

# =================================
# Example to demonstrate iterator
# Create a string and convert it into iterator
# Now, Use next method to print character of string


# ====================================
# Create an Alphabet class and implement it as iterable



# ======================================
# Example to show that dictionary is an iterable
# Create a dictionary and iterate through its values



# ===================================
# Create a class that returns values from fibonacci
# sequence each time next is called
# Sample output:
# Fib : 1
# Fib : 2
# Fib : 3
# Fib : 5


# =======================================
#           List Comprehension
# =======================================

# Multiply every value in the range(1, 11) using map and
# then using list comprehension
# Use filter to print odd nos from 1 to 10 and do
# the same using list comprehension


# ==============================
# Generate 50 values
# Take each value to power of 2
# Return multiples of 8
# Solve the above program using 2 approaches
# 1. Use list comprehension and filter only in single line
# 2. Use list comprehension, filter and map in single line



# ==================================================
# Generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# You will have to use list comprehension inside
# of list comprehension to solve the above challenge
# Use max of 2 lines to solve this problem



# ===================================================
# Create a multi dimensional list and
# print first column of the list using list comprehension
# Print diagnol elements using list comprehension


# ===================================================
#           Generator Functions
# ===================================================

# What is a generator?
# Genrerator is a function and a statement used,
# In order to prevent all values to be generated at once
# range() function uses generator

# Why do we use generators?
# Generators are used to in case of large data sets.
# Because large data sets will use more memory and thus
# slows down our os and program.
# A generator prevents all values to genrated at once, so
# we will get the value as we use it.


# ==========================================
# Create a generator to get a list of prime numbers
# Use yield keyword
# Note: If you use next() function after StopIteration,
# it will throw an error


# ============================================
#       Generator Expressions
# ============================================

# Generator expressions use parenthesis '()' in syntax

# =========================================
# Create a generator expression to generate doubles
# of num from 1 to 15
# Use next function to get next double

