# ==================================================
# ==================================================
#               Basics
# ==================================================
# ==================================================





# # Ask the user to input their name and store it in a variable called as name
#
# name = input("Enter your name? ")
#
# # Now print it on the screen
#
# print("Hello", name)
#

# ==================================================================

# Ask the user to input two values and store them in variables num1 and num2
#
# # num1 = input('Enter value of num1: ')
# # num2 = input("Enter value of num2: ")
# num1, num2 = input("Enter values: ").split()
#
# # Convert the values from string to numbers
# num1 = float(num1)
# num2 = float(num2)
#
# # Add the two values and store them in a variable sum
# sum = num1 + num2
#
# # Subtract the values and store them in a variable difference
# difference = num1 - num2
#
# # Multiply the values and store them in a variable product
# product = num1 * num2
#
# # Divide the two values and store them in a variable division
# division = num1 / num2
#
# # Raise the num1 to power of num2 and store in a variable exponential
# exponential = num1 ** num2
#
# # Divide the num1 by num2 and store the remainder in a variable remainder
# remainder = num1 % num2
#
# # Divide the num1 by num2 and store the result without decimal points in a variable floor
# floor = num1 // num2
#
# # print the results of the above calculations
# print("{} + {} = {}".format(num1, num2, sum))
# print("{} - {} = {}".format(num1, num2, difference))
# print("{} x {} = {}".format(num1, num2, product))
# print("{} / {} = {}".format(num1, num2, division))
# print("{} % {} = {}".format(num1, num2, remainder))
# print("{} ** {} = {}".format(num1, num2, exponential))
# print("{} // {} = {}".format(num1, num2, floor))
#

#=================================================================

# # Receive miles and convert to kilometers
# miles = input("Enter no. of miles: ")
#
# # convert miles string to float
# miles = float(miles)
#
# # Convert miles to km using formula : km = miles * 1.60934
# kms = miles * 1.60934
#
# # Print the kms
# print("{} miles equals {} kms".format(miles, kms))

#====================================================
# Enter calculation:
# 5 * 4

# # Ask the user for input and store them in seperate variables variable
# num1, operator, num2 = input("Enter Calculation: ").split()
#
# # convert the numbers from string to float
# num1 = float(num1)
# num2 = float(num2)
#
# # # if user entered + then we will perform addition and print result as per operator
# # if operator == '+':
# #     sum = num1 + num2
# #     print("{} + {} = {}".format(num1, num2, sum))
# # elif operator == '*':
# #     product = num1 * num2
# #     print("{} x {} = {}".format(num1, num2, product))
# # elif operator == "/":
# #     division = num1 / num2
# #     print("{} / {} = {}".format(num1, num2, division))
# # else:
# #     print("Currently {} is not supported.".format(operator))


# =======================================================================
# We will provide different output based on age
# 1 - 18 -> Important
# 20, 50, > 65 -> Important
# All others -> not important
#
# # Ask user to enter their age and convert it into int
# age = int(input("Enter Your age: "))
#
# # Check if age is between 1 and 18
# if (age >= 1) and (age <= 18):
#     print("Imporatnt")
# elif (age == 20) or (age == 50) or (age > 65):
#     print("Important")
# else:
#     print("Not Important")

# ==================================================================

# If age is 5: go to kindergarten
# ages 6 through 17: goes to grade 1 through 12
# If age is > 17: go to college
# Try to complete it in less than 10 or less lines of code.

# Ask user for input of age and convert in int
age = int(input("Enter your age: "))

# Check if age is 5
if age == 5:
    print("Go to kindergarten")

# check if age is 6 through 17
elif (age >=6) and (age <= 17):
    print('Go to class {}'.format(age - 5))

# check if age is > 17
elif age > 17:
    print("Go to college")

# Else if user enters invalid age such as -1
else:
    print("Invalid age.")