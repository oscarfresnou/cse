import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    fruit_total = 0
    clothes_total = 0
    for row in reader:
        if row[0] == "Region":
            continue
        item = row[2]
        profit_number = float(row[13])
        cost_number = row[12]
        revenue_number = row[11]

        if "Fruits" == item:
            fruit_total += profit_number
    print("Total Fruit Profit", round(fruit_total, 2))

    if "Clothes" == item:
        clothes_total += profit_number
print("Total Clothes Profit", round(clothes_total, 2))
print("Finished")

