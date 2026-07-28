import sys
def calculate_yearly_balances(
    initial_investment,
    monthly_contribution,
    annual_return,
    number_of_years
):
    yearly_balances = []
    current_balance = initial_investment
    monthly_return = annual_return / 100 / 12

    for year in range(number_of_years):
        for month in range(12):
            current_balance = current_balance * (1 + monthly_return)
            current_balance = current_balance + monthly_contribution

        yearly_balances.append(current_balance)

    return yearly_balances

initial_investment = float(input("Enter initial investment: £"))
monthly_contribution = float(input("Enter monthly contribution: £"))
annual_return = float(input("Enter expected annual return (%): "))
number_of_years = int(input("Enter number of years: "))

if initial_investment < 0:
    print("Initial investment cannot be negative.")
    sys.exit()

if monthly_contribution < 0:
    print("Monthly contribution cannot be negative.")
    sys.exit()

if annual_return < 0:
    print("Annual return cannot be negative.")
    sys.exit()

if number_of_years <= 0:
    print("Number of years must be greater than zero.")
    sys.exit()

yearly_balances = calculate_yearly_balances(initial_investment, monthly_contribution, annual_return, number_of_years)

year = 1

for balance in yearly_balances:
    print(f"Year {year}: £{balance:.2f}")
    year = year + 1

total_contributions = (
    initial_investment 
    + monthly_contribution * 12 *number_of_years
)
final_balance = yearly_balances[-1]
investment_growth = final_balance - total_contributions

print("\nInvestment Summary")
print(f"Total contributions: £{total_contributions:.2f}")
print(f"Investment growth: £{investment_growth:.2f}")
print(f"Final balance: £{final_balance:.2f}")




