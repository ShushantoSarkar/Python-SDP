# This file contains the welcome, square and login authentication fucntions

def welcome(fname, lname):
    print("First Name = ", fname)
    print("Last Name = ", lname)


def square(n):
    print(n*n)


pi = 3.14514


def login (username,password):
    if username == password:
        print("You have login successfully")
    else:
        print("You have extered wrong credentials")