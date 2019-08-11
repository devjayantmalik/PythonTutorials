# ==================================================
# ==================================================
#               Loops
# ==================================================
# ==================================================






# # Using for loop print a list of values
#
# for i in [1,2,3,4,5,6]:
#     print(i, end=" ")
#
# # ==========================================================
# # Use range function to generate a list of values in 3 different ways.
# # range(end) --> creates a list of items from 0 to end excluding end.
#
# # range(start, end) --> creates a list of items form start to end excludiing end.
#
# # range(start, end, step) --> creates a list of items from start to end and incrementing or decrementing the next number by step value.
# print()
# for i in range(5):
#     print(i, end=" ")
#
# print()
# for i in range(1,5):
#     print(i, end=" ")
#
# print()
# for i in range(1,10,2):
#     print(i, end=" ")
#
# print()
#
# # =====================================================
# # Print all even and odd numbers from zero to 200
# # using for loop and range function
# # Also store even and odd nums in list seperately.
#
# odds = []
# evens = []
#
# # Generate numbers from zero to 200 and loop through them
# for i in range(200):
#     if (i % 2) == 0:
#         evens.append(i)
#     else:
#         odds.append(i)
#
# print("Odds: ", end=" ")
# for i in odds:
#     print(i, end=" ")
#
# print("\nEvens: ", end=" ")
# for i in evens:
#     print(i, end=" ")
#
# print()
#
# # Ask User to enter a floating point number and
# # print the same number with two digits after the decimal
#
# number = float(input("Enter a float number: "))
#
# print("{:.2f}".format(number))
#
#
# # Have the user enter their investment amount and expected interest.
# # Each year their investment will increase by:
# # investment + (investment * interest)
# # Print out the earning after 10 years
#
# # Ask the user to enter investment, and expected interest
# investment = input("How much money would you like to invest: ")
# expectedInterest = input("How much interest rate would you like to get: ")
#
# # Convert the numbers to float to perform calculations.
# investment = float(investment)
#
# # Convert value to float and round the percentage digits by two digits
# expectedInterest = float(expectedInterest) * 0.01
#
#
# # Cycle through 10 years
# for year in range(1, 11):
#     investment = investment + (investment * expectedInterest)
#
# print("After 10 years the amount will be: {:.2f}".format(investment))
#
# # ===========================================================
# # Example to demonstrate that floating point numbers loose precision
# # Floats have precision of 16 digits in python
# i = (0.1 + 0.1 + 0.1) - 0.3
# print(i)
#
# # 0.x where x contains 32 digits
# i = 0.11111111111111111111111111111111
# j = 0.00000000000000010000000000000000
#
# print("{:.32f}".format(i +j))
#
# #======================================
# # Example to demonstrate order of operations
# # Multiplication and division have higher priority than + and -
#
# print("2 + 3 * 4 = {}".format(2 + 3 * 4))
# print("(2 + 3) * 4 = {}".format((2 + 3) * 4))
#
# # ======================================================
# # Generate a random number in range between 1 and 51
# # Now print all numbers from 1 to random number
# # Use while loop to solve this problem.
# # Use randrange() function to generate random number.
#
# # Import module
# import random
#
# # Generates a random number excluding 51
# randomNumber = random.randrange(1,51)
#
# # Declaring a variable to use in while loop for condition check
# i = 1
#
# while (i != randomNumber):
#     i += 1
#     print(i, end=" ")

# # =============================================
# # Examples to demonstrate continue and break
# # continue: jumps to start of the loop
# # break : exits the execution of the loop
# # Demonstrate using both for loop and while loop
#
# for i in range(1, 20):
#     if i == 5:
#         print("Before Continue...")
#         continue
#         print("After Continue....")
#     else:
#         print(i, end=" ")
#
# print("\nWe are out of loop...")
#
# for i in range(1, 20):
#     if i == 5:
#         print("Before break...")
#         break
#         print("After Break...")
#     else:
#         print(i, end=" ")
#
# print("We are out of loop...")
#
#
# # ==================================================
# # Use while loop to iterate 20 times
# # If a number is complete divisible by 2 then don't print it else print the number.
# # Use continue keyword to solve the problem.
#
# i = 1
#
# while i <= 20:
#     if (i % 2) == 0:
#         i += 1
#         continue
#     else:
#         i += 1
#         print(i, end=" ")
#
# print("\nWe are out of the loop....")
#

# ===========================================================
# Draw a pine tree on the screen
# Tips:
# 4 spaces : 1 hash
# 3 spaces : 3 hashes
# 2 spaces : 5 hashes
# 1 spaces : 7 hashes
# o spaces : 9 hashes


# Sample output:
# How tall is the tree: 5
#            #
#           ###
#          #####
#         #######
#        #########
#           #

# User entered : 5
rows = int(input('How long is the tree: '))

# space = 4
spaces = rows - 1

# hashes = 9
hashes = 1


# Create 5 rows

# In first row:
#   print " " * spaces
#   spaces -= 1
#   print "#" * hashes
#   hashes += 2

for row in range(rows):
    # Print spaces
    print(" " * spaces, end="")
    spaces -= 1
    # Then print hashes
    print("#" * hashes, end="")
    hashes += 2
    #Then print a new line
    print()


print(" " * int(rows - 1), end="")
print("#")

