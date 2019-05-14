# Date: 07/04/2018
# Author: Hanrui Tang
# Renters Choices
# 1. To determine renter's eligibility

#  define function to test applicants' eligibility

def eligibility_test(is_felon, credit_score, monthly_income, num_renters, base_rent):
    if is_felon == "yes":
        return False
    if credit_score <= 579:
        return False
    if monthly_income < base_rent * 3:
        return False
    if num_renters > 3:
        return False
    else:
        return True

# define function to calculate monthly rent

def monthly_rent(base_rent, has_pet, credit_score):
    if has_pet == "yes" and credit_score < 740:
        return base_rent + 100
    if has_pet == "yes" and credit_score >= 740:
        return base_rent * 0.9 + 100
    if has_pet == "no" and credit_score >= 740:
        return base_rent * 0.9
    else:
        return base_rent

# define function to calculate monthly rent per person

def monthlyrent_per(monthly_rent, num_renters):
    return monthly_rent / num_renters

# define function to calculate down-payment

def down_payment(monthly_rent):
    return monthly_rent * 2 + 250

# input renters' data

while True:
    is_felon = input("Are you a convicted felon? (yes or no)")
    credit_score = int(input("What is the your lowest credit score?"))
    monthly_income = int(input("What is your total monthly income?"))
    num_renters = int(input("How many renters?"))
    base_rent = float(input("What is base rent"))
    has_pet = input("Do you have a cat or dog?(yes or no)")

# Calculate rent

    if not eligibility_test(is_felon, credit_score, monthly_income, num_renters, base_rent):
        print("Thank you for your interest! Unfortunately, your application was rejected.")
    else:
        print("Congratulations! Your application was approved")
        print("Your monthly rent is", round(monthly_rent(base_rent, has_pet, credit_score), 2))
        print("Your monthly rent per person is", round(monthlyrent_per(base_rent, num_renters), 2))
        print("Your upfront down-payment is", round(down_payment(base_rent), 2))



