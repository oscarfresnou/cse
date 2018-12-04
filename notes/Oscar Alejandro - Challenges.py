'''
def challenge1 (first_name, last_name):
    print("So your name is %s, %s" % (last_name, first_name))


challenge1("Oscar", "Alejandro")
'''
'''
def challenge2(numbers):
    number = int(input("Enter a number: "))
    mod = number %2
    if mod > 0:
        print("This is an odd number")
    else:
        print("This is a even number")

challenge2(input)
'''
'''
def challenge3(base, height):
    b = int(input("Input the base: "))
    h = int(input("Input the height : "))

    area = b * h / 2

    print("area = %d" % area)


challenge3(input, input)
'''
def challenge4():