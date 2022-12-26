import click
from utils import (
    BANK_FINANCING_PERCENTAGE,
    get_monthly_costs,
    get_initial_investment,
    compute_mortgage_payments
)


@click.command()
@click.option('--purchase_price', help='Purchase price.', type=click.FLOAT)
@click.option('--loan_interest_rate', help='Loan interest rate.', type=click.FLOAT)
@click.option('--loan_num_years', help='Loan num years.', type=click.INT)
@click.option('--monthly_rent', help='Expected monthly rent.', type=click.FLOAT)
@click.option('--margin', help='Expected free cash flow margin', type=click.FLOAT)
@click.option('--mortgage_amount', help='Mortgage amount.', default=None, type=click.FLOAT)
def compute_initial_investment(purchase_price: float, loan_interest_rate: float, loan_num_years: int, monthly_rent: float, margin: float, mortgage_amount: float = None):
    """Compute the needed initial investment to get a profitable investment

    Args:
        purchase_price (float): Purchase price
        interest_rate (float): Loan interest rate
        num_years (int): Loan num years
        monthly_rent (float): Expected monthly rent
        margin (float): Expected free cash flow margin
    """
    return _compute_initial_investment(purchase_price, loan_interest_rate, loan_num_years, monthly_rent, margin, mortgage_amount)


def _compute_initial_investment(purchase_price: float, loan_interest_rate: float, loan_num_years: int, monthly_rent: float, margin: float, mortgage_amount: float = None):
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
        purchase_price, mortgage_amount, loan_interest_rate, loan_num_years)
    if (monthly_rent/monthly_costs) >= (1+margin):
        initial_investment = get_initial_investment(
            purchase_price, mortgage_amount)
        mortgage_payment = compute_mortgage_payments(
            principal=mortgage_amount,
            anual_interest_rate=loan_interest_rate,
            num_years=loan_num_years
        )
        monthly_fcf = monthly_rent - monthly_costs
        print(
            f"Initial investment: {initial_investment} \n"
            f"Mortgage: {mortgage_amount} \n"
            f"Monthly FCF: {monthly_fcf} \n"
            f"Monthly cost: {monthly_costs} \n"
            f"Mortgage payment: {mortgage_payment}")
    else:
        mortgage_amount = mortgage_amount - 1000
        return _compute_initial_investment(purchase_price, loan_interest_rate, loan_num_years, monthly_rent, margin, mortgage_amount)


if __name__ == '__main__':
    compute_initial_investment()
