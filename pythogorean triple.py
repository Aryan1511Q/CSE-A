print("Enter  the number in increasing order")
a=eval(input("Enter first number\n"))
b=eval(input("Enter second number\n"))
c=eval(input("Enter third number\n"))
d=a^2+b^2
e=c^2
if d==e:
    print(f"The entered numbers {a},{b},{c} are pythogorean numbers")
else:
    print(f"The entered numbers {a},{b},{c} are not pythogorean numbers")
