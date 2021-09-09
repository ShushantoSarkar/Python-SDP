# Armstrong operation
def armstrong():

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

# Fabnocci
def fabnocci():
        len = int(input("Enter the length of the series : "))
        series = 0
        n1 = 0
        n2 = 1

        print(n1,n2,end=" ")

        for len in range (2,len+1):
            series = n1+n2
            print(series,end=" ")
            n1 = n2
            n2 = series


#Factorial
def factorial():
    num = int(input("Enter a Number : "))
    facto = 1
    for num in range (1,num+1):
        facto = facto * num

    print("Factorial of",num ,"is = ", facto)


#LCM and HCF/GCD
def lcm_hcf():

    # L.C.M
    num1 = int(input("Enter first Integer : "))
    num2 = int(input("Enter second Integer : "))

    if(num1>num2):
        greater = num1
    else:
        greater = num2

    while(True):
        if(greater%num1 == 0) and (greater%num2 == 0):
            lcm = greater
            break
        greater+=1

    print("LCM = ",lcm)

    #H.C.F / G.C.D
    while(num1!=num2):
        if(num1>num2):
            num1 -= num2
        else:
            num2 -= num1

    print("H.C.F = ",num1)



# Leap_Year
def leap_year():
    year = int(input("Enter the Year : "))

    if(year%400 == 0):
        print("Its a Leap Year")
    elif(year%100 == 0):
        print("Its not a Leap Year")
    elif(year%4 == 0):
        print("Its a Leap Year")
    else:
        print("Its not a Leap Year")



# Max and Min value
def max_min():

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


# Palindrom
def palindrom():

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



# Sum of Natural Numbers
def sonn():
    num = 0
    sum = 0
    for num in range (1,11):
        sum = sum + num

    print("The sum of Natural no. form 1 to 10 is ", sum)



# Zip funciton Example
def zipFn():
    a = input("Enter the elements of first List = ")
    b = input("Enter the elements of second List = ")

    res = "\n".join("{} {}".format(x, y) for x, y in zip(a, b))
    print(res)



# Landing Page ( Menu )
print("=================================================================")
print("=================================================================")
print("  1. Armstrong")
print("  2. Fabnocci series")
print("  3. Factorial")
print("  4. Lcm, Hcf/Gcd")
print("  5. Leap Year")
print("  6. Max and Min value")
print("  7. Palindrom Number")
print("  8. Sum of first 10 natural No.")
print("  9. Zip function")
num = int(input("\n\nChose a Number to perfom the task : "))

if(num == 1):
    print("\nYou are in Armstrong Function\n")
    armstrong()
elif(num ==2):
    print("\nYou are in Fabnocci Fuction\n")
    fabnocci()
elif(num == 3):
    print("\nYou are in Factorial Fucntion\n")
    factorial()
elif(num == 4):
    print("\nYou are in LCM and HCF Function\n")
    lcm_hcf()
elif(num == 5):
    print("\nYou are in Leap Year Function\n")
    leap_year()
elif(num == 6):
    print("\nYou are in Max and Min Function\n")
    max_min()
elif(num == 7):
    print("\nYou are in Palindrom Function\n")
    palindrom()
elif(num == 8):
    print("\nYou are in Sum of Natural Number Function\n")
    sonn()
elif(num == 9):
    print("\nYou are in Zip Function\n")
    zipFn()

else:
    print("Invalid Input")
