


monthly_income = input("Enter your monthly income: ")
monthly_income = float(monthly_income)

monthly_expense = input("Enter your total monthly expenses :")
monthly_expense = float(monthly_expense)

monthly_savings = monthly_income - monthly_expense
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $",Projected_Savings)


