ESTIMATED_COST_PERCENTAGE=12


def compute_mortgage_payments(principal: float, anual_interest_rate: float, num_years: int) -> float:
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

