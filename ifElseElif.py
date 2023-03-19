# Escritura de instrucciones if

#! >>> IF

a = 97
b = 55
# test expression
if a < b:
    # statement to be run
    print(b);

c = 93
d = 27
if c >= d:
    print(c);

#! >>> IF ELSE

a = 24
b = 44
if a <= 0:
    print(a)
else:
    print(b)

#! >>> IF ELIF 

a = 93
b = 27
if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")

#! >>> IF ELIF ELSE

a = 93
b = 27
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")   

#! More examples

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")