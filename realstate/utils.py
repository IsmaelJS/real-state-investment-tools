ESTIMATED_COST_PERCENTAGE = 12
ANNUAL_COST_PERCENTAGE = 1
BANK_FINANCING_PERCENTAGE = 0.8


def compute_mortgage_payments(
        principal: float, anual_interest_rate: float, num_years: int) -> float:
    """
    Calculates Amortization Amount per month
    :param principal: Principal amount
    :param anual_interest_rate: Anual interest rate
    :param num_mont: Total number of years
    :return: Amortization amount per month
    """
    adjusted_interest = anual_interest_rate / 12
    x = (1 + adjusted_interest) ** (num_years*12)
    return round(principal * (adjusted_interest * x) / (x - 1), 2)


def compute_purchase_costs(purchase_price: float) -> float:
    """
    Compute additional purchase costs due to taxes and administrative
    :param purchase_price:
    :return purchase costs
    """
    return ESTIMATED_COST_PERCENTAGE / 100 * purchase_price


def compute_anual_cost(
        purchase_price: float, annual_cost_percentage=ANNUAL_COST_PERCENTAGE) -> float:
    """
    Compute estimated anual cost
    :param purchase_price
    :param annual_cost_percentage
    :return anual cost
    """
    return annual_cost_percentage / 100 * purchase_price


def get_initial_investment(purchase_price: float, mortgage_amount: float) -> float:
    """
    Compute initial investment
    :param purchase_price
    :param mortgage_amount
    :return initial investment
    """
    initial_costs = compute_purchase_costs(purchase_price)
    return (purchase_price-mortgage_amount) + initial_costs


def get_monthly_costs(
        purchase_price: float, mortgage_amount: float, anual_interest_rate: float, num_years: int):
    """
    Compute monthly costs
    :param purchase_price
    :param mortgage_amount
    :param anual_interest_rate
    :param num_years
    :return monthly costs
    """
    mortgage_payment = compute_mortgage_payments(
        principal=mortgage_amount,
        anual_interest_rate=anual_interest_rate,
        num_years=num_years
    )
    monthly_costs = compute_anual_cost(purchase_price=purchase_price) / 12
    return mortgage_payment + monthly_costs


def compute_initial_investment(
        purchase_price: float, interest_rate: float, num_years: int,
        monthly_rent: float, margin: float, mortgage_amount: float = None):
    """Compute the needed initial investment to get a profitable investment

    Args:
        purchase_price (float): Purchase price
        interest_rate (float): Loan interest rate
        num_years (int): Loan num years
        monthly_rent (float): Expected monthly rent
        margin (float): Expected free cash flow margin
    """
    if mortgage_amount == None:
        mortgage_amount = BANK_FINANCING_PERCENTAGE * purchase_price
    monthly_costs = get_monthly_costs(
        purchase_price, mortgage_amount, interest_rate, num_years)
    if (monthly_rent/monthly_costs) >= (1+margin):
        return (get_initial_investment(purchase_price, mortgage_amount),
                mortgage_amount, monthly_costs)
    else:
        mortgage_amount = mortgage_amount - 1000
        return compute_initial_investment(
            purchase_price, interest_rate, num_years, monthly_rent, margin, mortgage_amount)
