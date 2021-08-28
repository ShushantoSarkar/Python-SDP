# WAP to swap values without using 3rd variable.

a = int(input("Enter First Value (A) : "))
b = int(input("Enter Second Value (B) : "))

print("Values before Swaping : \nA =" ,a , "\nB =" ,b)

a = a-b
b = a+b
a = b-a

print("Values before Swaping : \nA =" ,a , "\nB =" ,b)

