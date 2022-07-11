print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?"))

percent = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))


tip_perecent_plus_one = 1 + percent / 100

total = bill * tip_perecent_plus_one

per_person = total / people

print("Each person should pay " + ("${:.2f}".format(per_person)))