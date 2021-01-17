# ex1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(thisset)

# ex2
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

# ใช้เวลาไม่เอาตัวซ้ำกันในlist
result = []
number_list = [1, 1, 1, 2, 2, 3, 3, 3]

# ex1
for number in number_list:
    if not number_list:
        result.append(number)

# ex2
print(list(set(number_list)))