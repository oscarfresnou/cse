import csv

test_num = "4556737586899855"


def validate(num: str):
    if len(num) == 16:
        last_num = int(num[15])
        list_form = list(num)
        list_form.pop(15)
        reverse_form = list[::-1]
        print(reverse_form)
        for index in range(len(reverse_form)):

            return False


print(validate(test_num))


def check_second_digits(num):
    length = len(num)
    sum = [0]
    for i in range(length-2,-1,-2):
        number = eval(num[i])
#        number = number *
#      if number > 9:
#        str_Number = str(number)
#        number = eval(str_Number[0]) + eval(str_Number[1])
#        sum += number
#        return sum


def odd_digits(num):
    length = len(num)
    sum_odd = 0
    for i in range(length-1,-1,-2):
        num += eval(num[i])
    return sum_odd


def c_length(num):
    length = len(num)
    if num >= 13 and num <= 16:
        if num [0] == "4" or num [0] == "5" or num [0] == "6" or (num [0] == "3" and num [1] == "7"):
            return True
    else:
        return False


def main():
    filename = input("What is the name of your input file? ")
    infile= open(filename,"r")
    cc = (infile.readline().strip())
    print(format("Card Number", "20s"), ("Valid / Invalid"))
    print("------------------------------------")
    while cc!= "EXIT":
        even = check_second_digits(num)
        odd = odd_digits(num)
        c_len = c_length(num)
        tot = even + odd

        if c_len == True and tot % 10 == 0:
            print(format(cc, "20s"), format("Valid", "20s"))
        else:
            print(format(cc, "20s"), format("Invalid", "20s"))
        num = (infile.readline().strip())