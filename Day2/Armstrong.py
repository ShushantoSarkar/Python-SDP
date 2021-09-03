#WAP to find the number is Armstrong or not.

number = int(input("Enter a Number : "))
num = number
sum = 0
while( num>0 ):
    rem = num%10
    num = num//10
    cube = rem*rem*rem
    sum += cube 

if(sum == number):
    print(number," is a Armstrong number ")
else:
    print(number," is not an Armstrong number")
