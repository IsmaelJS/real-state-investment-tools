
# Real state investment tools

This project aims to provide the tools right to assess investments in real state assets.  

# Set environment vars
Edit the variable values in [.env](.env) file.

 - **PURCHASE_PRICE**. The market price of the asset. *E.g 170000*
 - **LOAN_INTEREST_RATE**. The interest rate of the loan. If the loan is variable type, it is recommended to set the maximum interest expected during the life of the loan. *Eg. Set 0.01 for 1% interest rate.*
 - **LOAN_NUM_YEARS**. The duration of the loan in years. *E.g. 30*
 - **MARGIN**. The expected margin over the breakeven point, considering the mortgage amortization as a cost. *E.g. Set 0.1 for 10% of margin.*
 - **MONTHLY_RENT**. Expected monthly rent. *E.g. 750*
 - **MORTGAGE_AMOUNT**. Mortgage amount. *E.g. 130000*
## Using the tools
### Compute required initial investment and mortgage
This function returns the initial investment and mortgage amount required for a profitable investment taking as inputs the purchase price, loan interest rate, loan duration, expected rent and margin.

Input

    make initenv
    make compute_initial_investment

Output

     python3 realstate/initial_investment.py \
       --purchase_price 170000 \
       --loan_interest_rate 0.0136 \
       --loan_num_years 30 \
       --monthly_rent 750 \
       --margin 0.45 \
       --mortgage_amount 160000

    Initial investment: 80400.0
    Mortgage: 110000.0
    Monthly FCF: 236.0433333333333
    Monthly cost: 513.9566666666667
    Mortgage payment: 372.29
