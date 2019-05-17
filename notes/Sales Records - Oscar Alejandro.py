import csv

with open("Sales Records.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    print("Processing...")
    fruit_total = 0
    clothes_total = 0
    Meat_total = 0
    Beverages_total = 0
    Office_Supplies_Total = 0
    Cosmetics_Total = 0
    Snacks_Total = 0
    Household_Total = 0
    Cereal_Total = 0
    Baby_Food_Total = 0
    Vegetables_Total = 0
    Personal_care_Total = 0
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
        if "Cosmetics" == item:
            Cosmetics_Total += profit_number
        if "Snacks" == item:
            Snacks_Total += profit_number
        if "Household" == item:
            Household_Total += profit_number
        if "Cereal" == item:
            Cereal_Total += profit_number
        if "Baby Food" == item:
            Baby_Food_Total += profit_number
        if "Vegetables" == item:
            Vegetables_Total += profit_number
        if "Personal Care" == item:
            Personal_care_Total += profit_number
    print("Total Fruit Profit", round(fruit_total, 2))
    print("Total Clothes _Profit", round(clothes_total, 2))
    print("Total Beverages Total", round(Beverages_total, 2))
    print("Total Meat Total", round(Meat_total, 2))
    print("Office Supplies Total", round(Office_Supplies_Total, 2))
    print("Cosmetics Total", round(Cosmetics_Total, 2))
    print("Snacks Total", round(Snacks_Total, 2))
    print("Household Total", round( Household_Total, 2))
    print("Cereal Total", round(Cereal_Total, 2))
    print("Baby Food", round(Baby_Food_Total, 2))
    print("Vegetables", round(Vegetables_Total, 2))
    print("Personal Care", round(Personal_care_Total, 2))

the_profits = [Baby_Food_Total, Vegetables_Total, Personal_care_Total, Meat_total, Snacks_Total, Beverages_total,
               Cereal_Total, Cosmetics_Total, Office_Supplies_Total, fruit_total, Household_Total, clothes_total]

index = the_profits.index(max(the_profits))

name_profit = ["Baby Food", "Vegetables", "Personal Care", "Meat", "Snacks", "Beverages", "Cereal",
               "Cosmetics", "Office Supplies", "Fruit", "Household", "Clothes"]

print("The most profitable items to sell are", name_profit[index], "with a total profit of", max(the_profits))


