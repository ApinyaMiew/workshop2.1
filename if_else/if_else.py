#ex1
a = 33
b = 200

if b > a:
    print("b is greater than a")

#ex2
a = 33
b = 33

if b > a:
    print("b is greater than a")
else a == b:
    print("a and b are equal")

#ex3
a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

#ex4
 = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("a is greater than b")

#ex5
a = 2
b = 330

max = a if a > b else b
print(max)

#ex6
a = 200
b = 33
c = 500

if a > b and c> a:
    print("Both conditions are True")

#ex7
a = 200
b = 33
c = 500

if a > b or a > c:
    print("At least one of the conditions is True")

#ex8
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and alse above 20!")
    else:
        print("but not above 20.")