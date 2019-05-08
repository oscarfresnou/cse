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


def reverse(num: str):
    print(num)
    print(num[::-1])


def valid(num: str):
    reversed_version = reverse(num)
    for i in reversed_version:
        ...

    reverse("4696467524043400")
