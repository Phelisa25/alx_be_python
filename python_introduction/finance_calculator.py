monthly_income = int(input("Enter your monthly income: ")) #Ask user for their monthly income
monthly_expenses = int(input("Enter your total monthly expenses: ")) #Ask user for their monthly expenses
monthly_savings = monthly_income - monthly_expenses
rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * rate)
print ("Your monthly savings are", monthly_savings)
print ("Your projected annual savings (with interest) are", projected_savings)