Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name=input("Enter your name\n")
... age=int(input("Enter your age\n"))
... gender=input("Enter your Gender 'M' or 'F'\n")
... days_worked=int(input("Enter your working days\n"))
... if age >= 18 and age < 30:
...     if gender == 'M':
...         wages = 700 * days_worked
...     elif gender == 'F':
...         wages = 750 * days_worked
... elif age >= 30 and age <= 40:
...     if gender == 'M' or gender == 'F':
...         wages = 800 * days_worked
