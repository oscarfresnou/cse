import csv

def validate (num: str):
    first_num = int(num[0])
    if first_num == 4:
        return True
    return False

# with open("Book1.csv", 'r') as old_csv:
#    reader = csv.reader(old_csv)
#    for row in reader:
#         old_number = int(row[0]) + 1
#        old_number = row[0]
#        print(old_number)


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]     # String
            first_num = int(old_number[0])
            if validate(old_number):
                writer.writerow(row)
        print("Ok")

