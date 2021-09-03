#WAP to find the Max and Min number using simple if condition.

num1 = int(input("Enter 1 No. :"))
num2 = int(input("Enter 2 No. :"))
num3 = int(input("Enter 3 No. :"))
num4 = int(input("Enter 4 No. :"))
num5 = int(input("Enter 5 No. :"))

if(num1>num2) and (num1>num3) and (num1>num4) and (num1>num5):
    largest = num1
elif (num2>num1) and (num2>num3) and (num2>num4) and (num2>num5):
    largest = num2
elif (num3>num1) and (num3>num2) and (num3>num3) and (num3>num5):
    largest = num3
elif (num4>num1) and (num4>num2) and (num4>num3) and (num4>num5):
    largest = num4
else:
    largest = num5

print("\nMax no. is : ", largest)

if(num1<num2) and (num1<num3) and (num1<num4) and (num1<num5):
    smallest = num1
elif (num2<num1) and (num2<num3) and (num2<num4) and (num2<num5):
    smallest = num2
elif (num3<num1) and (num3<num2) and (num3<num3) and (num3<num5):
    smallest = num3
elif (num4<num1) and (num4<num2) and (num4<num3) and (num4<num5):
    smallest = num4
else:
    smallest = num5

print("\nMin no. is : ", smallest)
