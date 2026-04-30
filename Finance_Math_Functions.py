# Finance_Math_Functions.py
# --------  Question 1: Simple Interest
def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    """
    Calculate simple interest.
    Parameters:
    principal (float): The initial amount of money.
    rate (float): The annual interest rate (in percentage).
    time (float): The time the money is invested for (in years).

    Returns:
    float: The simple interest earned.
    """   
    return si
principal = 4500.00
rate = 7
time = 5
print(f"Principal: R{principal:.2f}, Rate: {rate}%, Time: {time} years")
print(f"Question 1: R{simple_interest(principal, rate, time):.2f}")


# --------  Question 2: Compound Interest ------- 
def compound_interest(principal, rate, time):
    ci = principal * (1 + rate / 100) ** time
    """
    Calculate compound interest.
    Parameters:
    principal (float): The initial amount of money.
    rate (float): The annual interest rate (in percentage).
    time (float): The time the money is invested for (in years).

    Returns:
    float: The compound interest earned.
    """   
    return ci
principal = 12000.00
rate = 6.5
time = 8
print(f"\nPrincipal: R{principal:.2f}, Rate: {rate}%, Time: {time} years")
print(f"Question 2: R{compound_interest(principal, rate, time):.2f}")


# --------  Question 3: Hire Purchase --------
def hire_purchase(cost_of_item, rate, time, deposit):
    hp = ((cost_of_item - deposit) * ((1 + rate / 100)* time)) / 36
    """
    Calculate the total amount to be paid for a hire purchase agreement.
    Parameters:
    cost_of_item (float): The cost of the item being purchased.
    rate (float): The annual interest rate (in percentage).
    time (float): The time the money is invested for (in years).
    deposit (float): The initial payment made towards the item.

    rate (float): The annual interest rate (in percentage).
    time (float): The time the money is invested for (in years).

    Returns:
    float: The total amount to be paid.
    """   
    return hp
cost_of_item = 22000.00
rate = 11
time = 3
dp_rate = 15/100
deposit = cost_of_item * dp_rate
print(f"\nCost of Item: R{cost_of_item:.2f}, Rate: {rate}%, Time: {time} years, Deposit: R{deposit:.2f}")
print(f"Question 3: R{hire_purchase(cost_of_item, rate, time, deposit):.2f}")


# --------  Question 4: Inflation Analysis --------
def inflation_analysis(current_price, inflation_rate, time):
    future_price = current_price * (1 + inflation_rate / 100) ** time
    """
    Calculate the future price of an item based on inflation.
    Parameters:
    current_price (float): The current price of the item.
    inflation_rate (float): The annual inflation rate (in percentage).
    time (float): The time in years for which to calculate the future price.

    Returns:
    float: The future price of the item after accounting for inflation.
    """   
    return future_price
#current_price = 1550.00
#inflation_rate = 5.5
#time = 12
#print(f"\nCurrent Price: R{current_price:.2f}, Inflation Rate: {inflation_rate}%, Time: {time} years")
#print(f"Question 4: R{inflation_analysis(current_price, inflation_rate, time):.2f}")
print(f"Question 4: R{inflation_analysis(1550.00, 5.5, 12):.2f}")


# --------  Question 5: Reducing Depreciation --------
def reducing_depreciation(cost, rate, time):
    rd = cost * (1 - rate / 100) ** time
    """
    Calculate the reducing balance depreciation.
    Parameters:
    cost (float): The initial cost of the asset.
    rate (float): The annual depreciation rate (in percentage).
    time (float): The time in years for which to calculate the depreciation.

    Returns:
    float: The depreciated value of the asset.
    """   
    return rd
#cost = 480000.00
#rate = 18
#time = 6
#print(f"\nCost: R{cost:.2f}, Rate: {rate}%, Time: {time} years")
#print(f"Question 5: R{reducing_depreciation(cost, rate, time):.2f}")
print(f"Question 5: R{reducing_depreciation(480000.00, 18, 6):.2f}")


# ---------  Question 6: Quarterly Compound Interest --------
def compound_interest_quarterly(principal, rate, time):
    ciq = principal * (1 + rate / 400) ** (4 * time)
    """
    Calculate compound interest compounded quarterly.
    Parameters:
    principal (float): The initial amount of money.
    rate (float): The annual interest rate (in percentage).
    time (float): The time the money is invested for (in years).

    Returns:
    float: The compound interest earned.
    """   
    return ciq
#principal = 95000.00
#rate = 9
#time = 4
#print(f"\nPrincipal: R{principal:.2f}, Rate: {rate}%, Time: {time} years")
#print(f"Question 6: R{compound_interest_quarterly(principal, rate, time):.2f}")
print(f"Question 6: R{compound_interest_quarterly(95000, 9, 4):.2f}")


# ---------  Question 7: Loan Accrual   --------
def loan_accrual(principal, rate, time):
    la = (principal * (1 + (rate / (12 * 100))) ** 12) - principal
    """
    Calculate the total amount to be paid on a loan after accruing interest.
    Parameters:
    principal (float): The initial amount of the loan.
    rate (float): The annual interest rate (in percentage).
    time (float): The time the loan is taken for (in years).

    Returns:
    float: The total amount to be paid after accruing interest.
    """   
    return la
principal = 30000.00
rate = 14
time = 1
print(f"\nPrincipal: R{principal:.2f}, Rate: {rate}%, Time: {time} years")
print(f"Question 7: R{loan_accrual(principal, rate, time):.2f}")
#print(f"Question 7: R{loan_accrual(30000, 14, 1):.2f}")


# --------  Question 8: Capital Doubling Time --------
def cap_double_time(principal, rate, total_amount):
    cd_time = (total_amount / (principal * (rate/100)))
    """
    Calculate the time required for an investment to double in value based on the Rule of 72.
    Parameters:
    rate (float): The annual interest rate (in percentage).

    Returns:
    float: The time in years required for the investment to double.
    """   
    return cd_time
