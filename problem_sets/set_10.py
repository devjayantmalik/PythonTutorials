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

