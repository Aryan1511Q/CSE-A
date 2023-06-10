Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> year = int(input("Enter a year: "))
... 
... if year % 400 == 0:
...    print(f"{year} is a leap year")
... elif year % 100 == 0:
...    print(f"{year} is not a leap year")
... elif year % 4 == 0:
...    print(f"{year} is a leap year")
... else:
...     print(f"{year} is not a leap year")
