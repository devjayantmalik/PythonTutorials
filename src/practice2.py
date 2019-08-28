
# ===========================================================
# Ask user to enter first name and last name seperated by spaces
# Then create an empty list
# Then Append the fName and lName to the list in form of dictionary
# Now print the list
# Sample Output:
# Enter your name: Jayant Malik
# list with dictionary item: [{'fName': 'Jayant', 'lName': 'Malik'}]


# ================================================
# Write a program that generates this sample output.
# Enter Customer (Yes, No) : y
# Enter Customer Name : Jayant Malik
# Enter Customer (Yes, No) : y
# Enter Customer Name : Mohit Sharma
# Enter Customer (Yes, No) : n
# Customers added are:
# Jayant Malik
# Mohit Sharma


# =======================================================
#           Recursive functions
# =======================================================


# Write a program to compute factorial of a number
# Ask user for input
# Use recursive function to solve the problem
# Use exception handling to check for invalid no passed inside factorial function
# If invalid input is provided print invalid input and exit the program


# =========================================================
# Write a program to calulate fibonachi series using recursive functions
# Conditions for fibonacchi:
# If no is 0 then return 0
# if no is 1 then reurn 0
# if not is neither 0 nor 1 then return fib(no - 1) + fib(no - 2)

# Sample output for 20 fibs:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

# ==================================================
# ==================================================
# Reading Writing Files, Tuples, Recursive Functions
# ==================================================
# ==================================================



# Explain few concepts related to Reading Files:
# os module, with statement, open function



# ===============================================
# Open a txt file in write mode and set its encoding to utf-8
# open the above file as myFile reference.
# use write function only for writing.
# Also make sure to close the file

# Write below text each in seperate line :
# Jayant Malik
# Mohit Sharma
# Nripender
# Shaurya Bhatnagar


# Note: write() does not add a new line at the end of text.



# =====================================================
# Write a program to open the first_file.txt for reading
# Now, after opening the file, print the contents of the file
# close the file
# Note: use readlines() and readline() and read() function for reading.
# Note: Demonstrate readline() buffer position issue and fix it by changing buffer position.


# Also check the file metadata by opening the file properties
# in file explorer on windows and nautilus on linux.




# =============================================================
# Write a program using file handling:
# use open() to open file
# Change postion of buffer using seek()
# use tell() to tell the position of buffer
# use read() to read data from file
# use readline() to read a single line of text
# use readlines() to read all lines of text and return each line as list element
# use write(), writelines() to write data to file
# Check if a file is writable using writable() function
# use close to close the file.

# use closed property to check if a file buffer is closed
# Retrieve file name using name property
# Retrieve file mode using mode property






# =====================================================================
#               Using os module
# =====================================================================

# Use os module to:
# Rename a file
# Remove a file
# Create a directory
# Change into directory
# Check current working directory
# Change mode of directory
# Remove a directory





# ======================================================
#           Back to files
# ======================================================

# Write a program that displays txt file contents in such format:
# Sample output:
# Line 1 : Jayant Malik
# Line 2 : Mohit Sharma
# Line 3 : Nripender
# Line 4 : Shaurya Bhatnagar

# Use while loop and readline() function to solve the problem
# Trick : figure out how to check if there is no further lines to read using if statement




# =====================================================
# Write a program to cycle through each line:
# and output no of words per line, and average word length per line




# ====================================================
#                       Tuples
# ====================================================
# Note: tuples cannot change their values.




# =====================================================
# Create a tuple
# Access the values of tuple using indexes
# Use slice to get first 3 values from the tuple
# Get length of tuple using length function
# Tuple concatenation using + symbol
# Check if a file is inside a tuple
# Print values of tuple using for loop
# Convert a list in tuple
# Convert a tuple into a list
# Get Minimum and maximum value in a tuple


# ==================================================
# ==================================================
#               Object Oriented programming
# ==================================================
# ==================================================

# What are:
# Objects, Fields, Methods, Class

# ==========================================
# Model an object human using object oriented programming
# Create a class
# Create a init method and explain self keyword
# Create methods and fields about a human

# Now we have above template setup
# Create 3 human named jayant, sahil, vikas




# ===========================================
# Getters and Setters
# Create a class Rectangle
# Create two fields: height and width
# Use of keywords :
# @property
# @variable_name.setter
# __variableName
#



# ======================================================================
# Create a warrior game where two warriors fight till one dies

# Help and Hints:
# Warriors Class:
# Warriors will have names, health, and attack and block maximums
# Warriors will have capibilities to attack and block random amounts

# attack method: random() * maxAttack
# block method: random() * minAttack

# Battle Class:
# Will have capibality of looping till one warrior dies.
# Warriors will each get a turn to attack each other

# Function gets 2 warriors:
# one warrior will attack the other

# Attacks and blocks should be integers


# Sample output:
'''
Tom attacked Paul and deals 1 damange
Paul is down to 9 health
Paul attacked Tom and deals 2 damange
Tom is down to 9 health
Tom attacked Paul and deals 5 damange
Paul is down to 5 health
Paul attacked Tom and deals 6 damange
Tom is down to 5 health
Tom attacked Paul and deals 8 damange
Paul is down to 2 health
Paul attacked Tom and deals 5 damange
Tom is down to 2 health
Tom attacked Paul and deals 10 damange
Paul is down to 0 health
Game Over
'''

# ==================================================
# ==================================================
#    Inheritence, Polymorphism, Magic Methods
# ==================================================
# ==================================================

# Super Class
# Sub Class

# Inheritence: a way of using fields and methods,
# from a super class into sub class

# Magic Method: The methods that allows us to use built in function
# of python on our classes or objects
# Example : print(Class_Name) Should print info related to class.
# Example : sum([rect1, rect2]) should add rectangle 1 and rectangle 2.
# The magic methods are described in the class body
# The methods starts with two underscores and end with two underscores


# =====================================
# Create a class Animal that has common properties of every animal
# Then create a reptiles class that inherits animal class
# Now use methods and fields of animal class in mammal class
# Use __str__ magic method in animal class and override in mammal class
# Use super method in override method to get exact str of
# animal class and append their nurseYoung status

#
# Hints:
# Fields of Animal : birthType="Unknown...",
#                   appearence="Unknown", blooded="Unknown"

# Fields of Mammal : birthType="born alive",
#                   appearence="hair or fur", blooded="warn blooded", nurseYoung=True

# Fields of Reptile class: birthType="born in an egg or born alive",
#                    appearence="dry scales", blooded="cold blooded", nurseYoung=True



# ===============================================
# Polymorphism: Poly means many, and morphism means forms
# hence polymorphism is a way to define any object with properties
# and use it as long as its fields or methods used in class exists

# In other languages such as c++, c# there is a concept of
# statically typed language that is we need to define datatype of variable
# before assigning it some value. As python is dynamically typed language
# we do not need to specify datatype of variable. it is inferred automatically

# Polymorphism: An object is passed to the function or class. You can use the
# object and its fields and methods if the passed object holds those in
# use fields and methods



# Example to demonstrate this concept :
# Create a function called as tell_me(someObject), here someObject is a
# variable that will be passed to the function
# Implement the function to print Class Name and someObject.birthType
# Inside main Call the function passing reptile and mammal object.



# ======================================================
#                   Magic Methods
# ======================================================

# Magic Methods : the special kind of methods that are used to
# define custom behaviour of some operator, method or object

# Properties:
# They start and end with two underscores

# They do not need to be invoked as other function: reptile1 + reptile2
# In above line + is defined a custom behaviour
# to add reptile1 and reptile2 using __add__ magic method

# Some Magic methods:
# __eq__ : equal
# __ne__ : not equal
# __lt__ : less than
# __gt__ : greater than
# __le__ : less than or equal to
# __ge__ : greater than or equal to
# __add__ : addition
# __sub__ : subtraction
# __mul__ : multiplication
# __div__ : division
# __mod__ : modulus



# ==========================================================
# Create a Time class with fields hour min sec
# Implement the add magic method to add two times
# Implement the string magic method to return time as 02:03:10 string
# The time class with work with 24 hour time

# Sample output:
# Time 1: 23:10:52
# Time 2: 23:05:15
# Added time: 22:16:07

