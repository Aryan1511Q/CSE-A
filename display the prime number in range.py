Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> start = int(input("Enter the starting number: "))
... end = int(input("Enter the ending number: "))
... 
... print("Prime numbers between", start, "and", end, ":")
... for num in range(start, end + 1):
...     if num > 1: 
...         for i in range(2, num):
...             if (num % i) == 0:
...                 break
...         else:
...             print(num, end=" ")
