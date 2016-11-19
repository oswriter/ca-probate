# ca-probate -- California Probate Commissions & Attorney Fees Calculator
# v. 0.2 (2016-11-18)
# Based on Cal. Probate Code secs. 10800-10814.

# Copyright 2016 S.M. Oliva <oswriter@skipoliva.com>
# Distributed under a BSD 2-Clause License

import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

message = "Welcome to the California Probate Fees & Commissions Calculator"
message += "\nby S.M. Oliva"
message += "\nThis program is published under a BSD 2-Clause license."
message += "\n\nPlease enter a dollar amount without any currency symbols ($) or commas (,)."
print(message)

while True:
    gross_estate = input("\nWhat is the value of the decedent's California gross probate estate? ")
    try:
        gross_estate = int(gross_estate)
    except ValueError:
        print("Please enter a dollar amount without any currency symbols ($) or commas (,).")
    else:
        break

# Calculation of statutory probate fees and commissions
# under Cal. Probate Code secs. 10800-10814.

while True:
    if gross_estate < 0:
        fee = 0
    elif gross_estate < 100001:
        fee = gross_estate * .04
    elif gross_estate < 200001:
        fee = 4000 + ((gross_estate - 100000) * .03)
    elif gross_estate < 1000001:
        fee = 7000 + ((gross_estate - 200000) * .02)
    elif gross_estate < 10000001:
        fee = 23000 + ((gross_estate - 1000000) * .01)
    elif gross_estate < 25000001:
        fee = 113000 + ((gross_estate - 10000000) * .005)
    else:
        print("For an estate of this size, reasonable fees must be determined by the court.")
        break
    fee = locale.currency( fee, grouping=True )
    message = "The personal representative and the attorney for this estate are each entitled to a maximum fee of " + fee + "."
    print(message)
    break    

