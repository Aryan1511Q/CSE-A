Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> food_rating = int(input("Enter food rating (1-5): "))
... service_rating = int(input("Enter service rating (1-5): "))
... ambience_rating = int(input("Enter ambience rating (1-5): "))
... bill_amount = float(input("Enter bill amount: "))
... 
... if food_rating >= 4 and service_rating >= 4 and ambience_rating >= 4:
...     tip = 0.1 * bill_amount
... elif food_rating >= 4 or service_rating >= 4 or ambience_rating >= 4:
...     tip = 0.05 * bill_amount
... else:
...     tip = 0.01 * bill_amount
... 
... print(f"Tip amount: Rs {tip}")
