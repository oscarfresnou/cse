# 3 print("Hello World!")
# print()
# This is a comment. I can write whatever i want
# Here and it won't do anything about it.
# It has no side effect on the code.
# print()  # This adds extra spaces on the terminal
# print("This will print here. Notice the spacing.")

a = 4
b = 3
print(a + b)
print(a*5)
print(5-3)
print(6/5)  # Results in a float (without decimals)

print("Figure this out")
print(6 // 4)
print(12 // 3)
print(9 // 4)


car_name = "The Wiebe Mobile"
car_type = "Tesla"
car_cylinders = "1024"
car_mpg = 0.01

print("I have a car called %s. It's pretty nice." % car_name)

# print(6 % 4)
# print(5 % 3)
# print(9 % 4)
# Auto-comment Ctrl + /
# age = input("How old are you")
# print()

# Hidden age
# real_age = int(input("How old are you? >_"))
# Hidden_age = "real_age + 5"
# print("Hidden_age")
# print("%d is incredibly old")
# functions
# def  printHelloWorld():
#  print("Hello World")

# print("hello world")

# f(x) = 2x + 3
# def f (x):
#  print(2*x + 3)

# Loops
# for i in (1,2,3)
# print()
# for i in range (100)
'''
Hint with loops:
For loops - Use when you know EXACTLY how many iterations
While loo[s - use when you dont know how many iterations
'''

# Random numbers
# import random
# Control Statements
# def grade_calc(percentage):
# if return "A"
#  elif percentage>= 80:
# return "B"
# elif percentage>= 70:
#  return "C"
#  elif percentage>= 60:
#  return "D"
# else:
#    return"F"

# print(grade_calc(60)

# Equality statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)
"""
a = 3 # A is set to 3
a == 3 # is equal to 3?
"""

# Lists
shopping_list = ["whole milk", "PC", "Eggs", "Trash (Xbox one)", "Other Trash(PS4)"]
print(shopping_list)
print(shopping_list[0])
print("The second thing on your list is %s" % shopping_list)
# print("The length of the list is %s") % len(shopping_list)

# changing elements in the list
shopping_list[0] = "2% milk"
print(shopping_list)
print(shopping_list[0])

# Looping through lists
for items in shopping_list:
    print(items)

# My List
my_list = ["water", "glue", "garbage bags", "foam plates"]
print(my_list)
my_list[2] = "garbage can"
print(my_list)
print("The last thing in the list is %s" % my_list[len(my_list) - 1])
print(my_list)

# Getting part of the list
print(my_list[1:3])
print(my_list[1:4])
print(my_list[1:])                    # This goes all the way to the end dont need another number
print(my_list[:2])

holiday_list = []  # ALWAYS USE SQUARE BRACKETS
holiday_list.append("Tacos")
holiday_list.append("bumblebee")
holiday_list.append("RDR2")
print(holiday_list)

# Notice this is "object.method(Parameters)"

# Removing things in list
holiday_list.remove("Tacos")
print(holiday_list)

'''
1. Make a new list with 3 items
2. Add a fourth item to the list
3. Remove one of the first three items on the list
'''
new_list = []
new_list.append("Pillow")
new_list.append("Hot Choclate")
new_list.append("Pen")
print(new_list)
new_list.remove("Pen")
new_list.append("The Grinch move")
print(new_list)

color = []
color.append("Blue")
color.append("Yellow")
color.append("Pink")
color.append("Salmon")
color.append("Red")
color.append("White")
color.append("Black")
color.append("cyan")
color.append("Purple")
color.append("Orange")
color.append("Gray")
color.append("Maroon")
color.append("Apricot")
color.append("Lavender")
print(color)

# changing things into a list
string1 = "cyan"
list1 = list(string1)
print(list1)

# changing lists into strings
print("cyan".join(list1))

for character in list1:
    if character == "u":
     current_index = list1.index(character)
     list1.pop(current_index)
    # list1.insert(current_index "*")