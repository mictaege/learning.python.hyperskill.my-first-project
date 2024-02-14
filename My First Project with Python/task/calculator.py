# Write your code here
earnings = {"Bubblegum": 202, "Toffee": 118, "Ice cream": 2250, "Milk chocolate": 1680, "Doughnut": 1075, "Pancake": 80}

print("Earned amount:")
for article, earning in earnings.items():
    print(f"{article}: ${earning}")
total_earning = sum(earnings.values())
print(f"Income: {total_earning}")

staff_expenses = int(input("Staff expenses:"))
other_expenses = int(input("Other expenses:"))

net_income =  total_earning - staff_expenses - other_expenses
print(f"Net income: ${net_income}")
