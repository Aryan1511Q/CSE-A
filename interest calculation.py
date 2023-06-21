def interest_calculation(name, age, gender, principal, years):
    if gender == 'M':
        if age >= 60:
            rate = 0.12
        else:
            rate = 0.09
    elif gender == 'F':
        rate = 0.1
    else:
        rate = 0.09
    
    interest = principal * rate * years
    total_amount = principal + interest
    
    return interest, total_amount


name = input("Enter customer name: ")
age = int(input("Enter customer age: "))
gender = input("Enter customer gender (M/F): ")
principal = float(input("Enter principal amount: "))
years = int(input("Enter number of years: "))


interest, total_amount = interest_calculation(name, age, gender, principal, years)


print(f"Customer Name: {name}")
print(f"Principal Amount: {principal}")
print(f"Interest Amount: {interest}")
print(f"Total Amount: {total_amount}")
