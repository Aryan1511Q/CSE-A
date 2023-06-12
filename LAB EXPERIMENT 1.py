Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=int(input("Enter any number\n"))
... if a%2==0:
...     print("It is even number")
...     b=str(a)
...     c=(b[::-1])
...     if str(a) == c :
...         print("it is a palindrome number\n")
...     else:
...         print("It is not a palindrome number\n")
... else:
...     print("it is odd number")
...     print(f"The factorial of {a} is")
...     for i in range(1,a+1):
...         if a%i==0:
