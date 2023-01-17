import re


'''a = "While some articles are of the highest quality of scholarship, others are admittedly complete rubbish. Also, since" \
    " Wikipedia can be edited by anyone at any time, articles may be prone to errors, including vandalism, so Wikipedia" \
    " is not a reliable source. So, please do not use Wikipedia to make critical decisions"
b =a.split(" ")
print(b)
print(a.find("rubbish"))
print(a[94:101])'''

#Reguler Expressions(Regex)
#example1:

'''a = "The PEP8 guide you quote suggests that it is okay to use a bare exception in your case provided you are logging " \
   "the errors. fail I would think that you should cover as many exceptions as you can/know how to deal with and then " \
   "log the rest and "
b = re.search("fail" , a)
print(b)

if  b:
    print("yes word is available in a")
else:
    print("no its not there in a")
a.count("fail")
'''
#EXample:2
'''a =(input("enter the mobile num"))

j = re.fullmatch("[7-9]\d{9}",a)

print(j)

if j:
    print("true")
else:
    print("false")'''

#Example:3

b = "When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type" \
"a particular data set could mean retention of meaning, and, it could mean an 123 increase in efficiency or security"

c = re.search("choosing" , b)
print(c)

if re.search("choosing" , b):
    print("yes its there in string")
else:
    print("not available in string")
#using-digits-in-regex

result = (re.findall(r"\d{3}" , b))
print(result)
print(type(result))

if result[0] == "123":
    print("pass")
else:
    print("fail")
#using-word-in-regex

ajay = (re.findall(r"\w{4}" , b))
print(ajay)

if ajay[6] == "type":
    print("Yes")
else:
    print("No")




