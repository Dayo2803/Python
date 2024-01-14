print("Welcome to tip Calculator.")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?? "))
friends = int(input("How many people to spilt the bill? "))
bill_tip_perc = tip / 100
total_tip = total * bill_tip_perc
total_bill = total + total_tip
each_bill = total_bill / friends
final_amount = round(each_bill, 2)
print(f"Each person should pay: ${final_amount}")