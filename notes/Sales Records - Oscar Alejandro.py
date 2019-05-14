import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    fruit_total = 0
    clothes_total = 0
    Meat_total = 0
    Beverages_total = 0
    Office_Supplies_Total = 0
    for row in reader:
        if row[0] == "Region":
            continue
        item = row[2]
        profit_number = float(row[13])
        cost_number = row[12]
        revenue_number = row[11]

        if "Fruits" == item:
            fruit_total += profit_number
        if "Clothes" == item:
            clothes_total += profit_number
        if "Beverages" == item:
            Beverages_total += profit_number
        if "Meat" == item:
            Meat_total += profit_number
        if "Office Supplies" == item:
            Office_Supplies_Total += profit_number
    print("Total Fruit Profit", round(fruit_total, 2))
    print("Total Clothes _Profit", round(clothes_total, 2))
    print("Total Beverages Total", round(Beverages_total, 2))
    print("Total Meat Total", round(Meat_total, 2))
    print("Office Supplies Total", round(Office_Supplies_Total, 2))

