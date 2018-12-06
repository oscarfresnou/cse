'''
def challenge1 (first_name, last_name):
    print("So your name is %s, %s" % (last_name, first_name))


challenge1("Oscar", "Alejandro")
'''

'''
def challenge2(numbers):
    if numbers % 2 == 0:
        print("This is a even number")
    else:
        print("This is a odd number")


challenge2(57)
'''

'''
def challenge3(base, height):
    area = base * height / 2
    print("area = %d" % area)


challenge3(4, 6)
'''

'''
def challenge4(number):

    number = int(input("Type a negative or a positive number"))
    if number < 0:
        print("This is a negative number")
    if number > 0:
        print("This is a positive")
    if number == 0:
        print("This is zero")


challenge4(50)
'''


def challenge5(radius):
    from math import pi
    r = float(input("Input the radius of the circle : "))
    print("The area of the circle with radius " + str(r) + " is: " + str(pi * r ** 2))

challenge5(50)

