SHELL := /bin/bash
include .env

install:
	pip install -r requirements.txt

initenv: 
	( \
       source env/bin/activate; \
       pip install -r requirements.txt; \
    )

compute_initial_investment:
	python3 realstate/initial_investment.py \
	 --purchase_price ${PURCHASE_PRICE} \
	 --loan_interest_rate ${LOAN_INTEREST_RATE} \
	 --loan_num_years ${LOAN_NUM_YEARS} \
	 --monthly_rent ${MONTHLY_RENT} \
	 --margin ${MARGIN} \
	 --mortgage_amount ${MORTGAGE_AMOUNT}

test:
	cd realstate && tox
