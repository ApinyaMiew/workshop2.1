# Ex1
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Ex2
string = "banana"
for char in string:
    print(char)

# Ex3
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# Ex4
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# Ex5
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
else:
    print("Finally finished!")

# Ex6
adjectives = ["small", "big"]
fruits = ["apple", "banana", "cherry"]

for adjective in adjectives:
    for fruit in fruits:
        print(adjective, fruit)