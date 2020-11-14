import re

i_percent = int(input("Hur mycket ränta vill \"banken\" ha?\n"))
inp = input("Hur mycket vill du låna och hur mycket kan du betala tillbaka varje månad?\n")
match = re.findall(r"\d+", inp)

origin_loan = int(match[0])
pay_per_month = int(match[1])
if (origin_loan * i_percent / 100) >= pay_per_month:
    print("Du kommer aldrig kunna betala tillbaka detta lån")
else:
    current_loan = origin_loan
    sum_interest = 0
    month = 0

    while current_loan > 0:
        interest = current_loan * i_percent / 100
        sum_interest = sum_interest + interest
        current_loan = current_loan + interest
        if current_loan > pay_per_month:
            current_loan = current_loan - pay_per_month
        elif current_loan <= pay_per_month:
            current_loan = 0
        month += 1

    print("Efter {} månader har du betalat tillbaka de {} kronorna samt {:0.1f} kr ränta".format(month, origin_loan, sum_interest))    
