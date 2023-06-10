Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number = int(input("Enter a number: "))
... 
... print("Factors of", number, ":",end=" ")
... for i in range(1, number + 1):
...     if number % i == 0:
...         print(i,end=" ")
