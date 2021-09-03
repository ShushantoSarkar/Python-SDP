#WAP to find the entered year is Leap year or not.  

year = int(input("Enter the Year : "))

if(year%400 == 0):
    print("Its a Leap Year")
elif(year%100 == 0):
    print("Its not a Leap Year")
elif(year%4 == 0):
    print("Its a Leap Year")
else:
    print("Its not a Leap Year")