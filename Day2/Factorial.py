#WAP to find the factorial of any number

num = int(input("Enter a Number : "))
facto = 1
for num in range (1,num+1):
    facto = facto * num

print("Factorial of",num ,"is = ", facto)