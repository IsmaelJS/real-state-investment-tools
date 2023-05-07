SHELL := /bin/bash
include .env

build_image:
	docker build --tag "investment_tools" .

compute_initial_investment:
	docker run investment_tools /bin/bash -c \
	"python initial_investment.py \
	 --purchase_price ${PURCHASE_PRICE} \
	 --loan_interest_rate ${LOAN_INTEREST_RATE} \
	 --loan_num_years ${LOAN_NUM_YEARS} \
	 --monthly_rent ${MONTHLY_RENT} \
	 --margin ${MARGIN} \
	 --mortgage_amount ${MORTGAGE_AMOUNT}"

test:
	docker run investment_tools /bin/bash -c "tox"
