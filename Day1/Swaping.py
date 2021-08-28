# WAP to Swap values using 3rd variable.


a = int(input("Enter First Value (A) : "))
b = int(input("Enter Second Value (B) : "))

print("Values before Swaping : \nA =" ,a , "\nB =" ,b)

c = a
a = b
b = c

print("Values after Swaping : \nA =" ,a , "\nB =" ,b)
