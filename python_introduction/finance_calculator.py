


monthly_income = input("Enter your monthly income: ")
monthly_income = float(monthly_income)

total_monthly_expense = input("Enter your total monthly expenses :")
total_monthly_expense = float(total_monthly_expense)

monthly_savings = monthly_income - total_monthly_expense
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $",Projected_Savings)


