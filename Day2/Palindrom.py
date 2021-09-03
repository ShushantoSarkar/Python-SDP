#WAP to find the input number is palindrom or not.

number = int(input("Enter a No.: "))

num = number
rev_num=0

while(num>0):
    rem = num%10
    num = num//10
    rev_num = (rev_num * 10) + rem

if(number==rev_num):
    print(number," is a Palindrom Number")
else:
    print(number," is not a Palindrom Number")

