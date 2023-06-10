Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> start = int(input("Enter the starting table: "))
... end = int(input("Enter the ending table: "))
... 
... print("Multiplication table from", start, "to", end, ":")
... for i in range(1, 11):
...     for j in range(start, end + 1):
...         result = j * i
...         print(j, "*", i, "=", result, end=" ")
...     print()
