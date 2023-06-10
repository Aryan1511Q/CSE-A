Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=input("Enter your Name\n")
... b=eval(input("Enter your salary\n"))
... c=eval(input("Enter your service year(in total)\n"))
... d=(b/100)*10
... e=(b/100)*8
... f=(b/100)*6
... if (c>10):
...     print(f"{a} your bonus amount is {d}")
... elif (c>6 and c<10):
...     print(f"{a} your bonus amount is {e}")
... else:
...     print(f"{a} your bonus amount is {f}")   
