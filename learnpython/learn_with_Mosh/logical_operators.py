# logical operators -- AND and OR, not
# if applicant has high income OR good credit, he can apply for the loan
# and cond - both condition should be true
# or cond - both cond or either of cond should be true

'''
has_good_credit = True
has_high_income = False

if has_good_credit or has_high_income:
    print("Eligible for loan")
'''

has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")




