missed_investment = {3:50000, 2:30000, 1:30000}

returns = 11

split_years = 1

total_missed = 0

for years in missed_investment:
    year_returns = missed_investment[years]
    for i in range(years):
        year_returns += (year_returns/100*returns)
    total_missed += year_returns

print("Your total missed investment is: ", total_missed)
#convert years to months

monthly_interest_rate = (returns / 12) / 100
months = years * 12
emi = (total_missed * monthly_interest_rate * (1 + monthly_interest_rate)**months) / \
        ((1 + monthly_interest_rate)**months - 1)

print("Your Extra investment per month to gain back returns is: ", emi)