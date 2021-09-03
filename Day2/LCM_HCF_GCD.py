#WAP to find the LCM , HCF and GCD

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