# WAP to reverse a 3 digit number.

num = int(input("Enter a 3 digit Number = "))

rem1 = num % 10  
num1 = num // 10  

rem2 = num1 % 10  
num2 = num1 // 10  

rem3 = num2 % 10  


print("Reverse Number = ", rem1,rem2,rem3)