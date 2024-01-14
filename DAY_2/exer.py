age = input("Enter your current age: ")

age_cpy = int(age)
years_rem = 90 - age_cpy
days_rem = years_rem * 365
weeks_rem = years_rem * 52
months_rem = years_rem * 12

print(f"you have {days_rem}, {weeks_rem} weeks, and {months_rem} months left.")