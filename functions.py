#FUNCTIONS:
'''a = int(input("enter the number"))
b = 24

c = (a+b)

print(c)'''

'''def adding(a, b):
    print(a+b)

adding(2,5)

def multi(b,a,s,w):
    print(a+b*s/w)

multi(3,5,0,1)

def div(a,b,c):
    print(a-b-c)
div(2,4,6)
def sub(a,b):
    print(b-a)
sub(4,3)
adding(2,3)'''

#odd even

'''a = int(input("enter the number"))
    b =20
    
if a%2 == 0:
    print(a, "its even")
else:
    print(a, "its odd")
def add_even(a):
    print(a)'''

# odd_even
#ajay = int(input("enter the number")) #global

'''def odd_even(ajay):               #local
    if ajay % 2 == 0:
        print(ajay, "is even")
    else:
        print(ajay, "is odd")

odd_even(20)
odd_even(50)
odd_even(15)
odd_even(39)'''

#FUNCTIONS EXMAPLE:
'''def ajay():
    print(2+3)
ajay()'''

'''1,1020,98,87,78
def adding(int1,int2,int3,int4,int5):
    print(int1+int2+int3+int4+int5)

def multi(int3,int4,int5):
    print(98*87*78)

def div(int2,int1):
    print(int2/int1)

def sub(a,b):
    print(a-b)

def all_aurthmetic(p,q,r,s,t):
    print(p+q-r*s/t)
sub(98,87)
adding(1,1020,98,87,78)
all_aurthmetic(23,69,96,89,3)
multi(98,87,78)

#Math Modules:

import math

ajay = 1024

print(math.sqrt(ajay))
print(math.ceil(ajay))
print(math.degrees(1024.08))
print(math.floor(23*34))
print(math.remainder(2.0,3.0))
print(math.pow(2.0,3.0))'''

#decesion making example:

'''ajay=int(input("enter the values of ajay"))
basu=int(input("enter the values of basu"))
shiva=int(input("enter the values of shiva"))

if ajay > basu and ajay > shiva:
     print("yes its greater than basu")

elif ajay < basu and ajay < shiva:
    print("yes its less than basu")

elif ajay < shiva:
    print("yes its less than shiva")

else:
  print("both values are equal")'''


'''brand =input("enter the brand")

    if brand == "nike":
        print("yes its populer brand")

    elif brand == "puma":
        print("yes its good brand")

    elif brand == "adidas":
        print("yes its adidas")
    else:
        print("not applicable")'''

#example:

'''def bigger_number():
    n1 = int(input("enter the number1"))
    n2 = int(input("enter the number2"))
    n3 = int(input("enter the number3"))
    if n1>n2 and n1>n3:
        print("biggest number is :",n1)
    elif n2>n3:
        print("bigger number is :",n2)
    else:
        print("biggest number is :",n3)

bigger_number()'''

#Functions Examples:

'''def add2number(x,y):
    print(x+y)
add2number(2,7)
add2number(x=2,y=7)

def wish(name,msg):
    print("hello",name,msg)
wish("ajay","hi")'''

'''def shiv(*n):  #n =1,3,4,5,6
    total = 0  #starting point
    for i in n: #ending point
        total = total+i
    print(total)
shiv(1,3,4,5,6,7,9)'''
#Example 2
'''def fun(**a):
    """

    :param a:
    :return:
    """
    print(type(a))
    for k, v in a.items():  #keys values always in dict
     print(k,"=",v)
    for k in a.keys():
        print(k)
    for v in a.values():
        print(v)

fun(a=10,b=78,c=90)'''

#example 4
'''def ajay(aj,ba):
    """

    :param aj: aj means ajay
    :param ba: ba means basu
    :return:
    """

    c = aj + ba
    return c
print(ajay(45,78))'''

a = "my name is basu"
print(a[3:7])