#WAP to find the fabnocci series

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
    