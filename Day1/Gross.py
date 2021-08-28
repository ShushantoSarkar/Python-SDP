# WAP to calculate gross sal for basic sal (HRA = 30%, TA =40%, DA=20% )

sal = int(input("Enter the Salary Amount : "))
HRA = (sal*30)/100
TA = (sal*40)/100
DA = (sal*20)/100
Gross = sal+HRA+TA+DA

print("HRA = ", HRA)
print("TA = ", TA)
print("DA = ", DA)
print("Gross = ", Gross)

