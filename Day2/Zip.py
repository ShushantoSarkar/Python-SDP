a = input("Enter the elements of first List = ")
b = input("Enter the elements of second List = ")

res = "\n".join("{} {}".format(x, y) for x, y in zip(a, b))
print(res)
