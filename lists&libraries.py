# simple list
nambers = [1, 2, 3, 4, 5]
people = ["Tom", "Bob", "Sam"]
# Crate empty lists
list1 = []
list2 = list()

objects = [1, 2.5, "What", True]

print(objects)

nums1 = [1, 2, 3, 4, 5]
nums2 = list(nums1)
print(nums2)

letters = list("Hello")
print(letters)

numbers = [5] * 6
print(numbers)

people = ["Tom", "Sam", "Bob"]
# Get elements
print(people[0])
print(people[1])
print(people[-1])

people[0] = "Diman"

print(people)

# Cycles with lists
# For
people = ["Tom", "Sam", "Bob"]
for person in people:
    print(person)

#While
people = ["Tom", "Sam", "Bob"]
i =0
while i < len(people):   # len - lenght of list
    print(people[i])
    i += 1

numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5])
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is not equal to numbers2")

# Methods and functions for list

people = ["Tom", "Bob"]

# add item to end of list
people.append("Alice")
# add item to the second point
people.insert(1, "Bill")
# add several item to the end of list
people.extend(["Mike", "Sam"])
# get index of item
index = people.index("Tom")
# remove item
remove = people.pop(index)
# remove the last item
last_item_remove = people.pop()
# Remove Alice
people.remove("Alice")

print(people)
# Clear all items
people.clear()

# Check item exist
people = ["Tom", "Bob", "Alice", "Sam"]
if "Alice" in people:
    people.remove("Alice")
print(people)

# Remove items with "del"

people = ["Tom", "Bob", "Alice", "Sam", "Bill", "Kate", "Mike"]
del people[1] # remove item with index 1
del people[:3]   # remove all items before fourth, not including it
print(people)   # ["Bill", "Kate", "Mike"]
del people[1:]   # remove all right items since second
print(people)   # ["Bill"]

# Count of item
people = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]
 
people_count = people.count("Tom")
print(people_count)

# Sort
people = ["Tom", "Bob", "Alice", "Sam", "Bill"]
 
people.sort()

people = ["Tom", "bob", "alice", "Sam", "Bill"]
 
sorted_people = sorted(people, key=str.lower)
print(sorted_people)

# people.reverse()
print(people)

# A problem with uppercase and lowercase letters
people = ["Tom", "bob", "alice", "Sam", "Bill"]
 
people.sort()
print(people)

people.sort(key=str.lower)
print(people)

# Min Max
numbers = [9, 21, 12, 1, 3, 15, 18]
print(min(numbers))     # 1
print(max(numbers))     # 21

# Copying lists
# Shallow copy. Change one of lists - change another
people1 = ["Tom", "Bob", "Alice"]
people2 = people1
people2.append("Sam")
print(people1)   # ["Tom", "Bob", "Alice", "Sam"]
print(people2)   # ["Tom", "Bob", "Alice", "Sam"]

# Deep copy
people1 = ["Tom", "Bob", "Alice"]
people2 = people1.copy()
people2.append("Sam")
# people1 и people2 match different lists
print(people1)   # ["Tom", "Bob", "Alice"]
print(people2)   # ["Tom", "Bob", "Alice", "Sam"]

# Copying part of list
people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
 
slice_people1 = people[:3]   # 0 to 3
print(slice_people1)   # ["Tom", "Bob", "Alice"]
 
slice_people2 = people[1:3]   # 1 to 3
print(slice_people2)   # ["Bob", "Alice"]
 
slice_people3 = people[1:6:2]   # 1 to 6 step 2
print(slice_people3)   # ["Bob", "Sam", "Bill"]

# Sum lists
people1 = ["Tom", "Bob", "Alice"]
people2 = ["Tom", "Sam", "Tim", "Bill"]
people3 = people1 + people2
print(people3)

# List of lists
people = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]
person = list()
person.append("Bill")
person.append(41)

people.append(person)

print(people[-1])

people[-1].append("+7898445355")

print(people[-1])

people[-1].pop()
print(people[-1])

people.pop(-1)

people[0] = ["Sam", 18]
print(people)

# list by cycle
people = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]
 
for person in people:
    for item in person:
        print(item, end=" | ")

# Tuple (Kortezh) there is no changable

tom = "Tom", 23
print(tom)

tom = ("Tom",)
print(tom)

# tuple from list
data = ["Tom", 37, "Google"]
tom = tuple(data)
print(tom)

name, age, company, position = ("Tom", 37, "Google", "software developer")
print(name)         
print(age)          
print(position)     
print(company)

def get_user():
    name = "Tom"
    age = 22
    company = "Google"
    return name, age, company

user = get_user()
print(user)

tom = ("Tom", 22, "Google")
for item in tom:
    print(item)

# Ranges

for i in range(5):
    print(i, end=" ")

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n")

# dictionary

users = {1: "Tom", 2: "Bob", 3: "Bill"}
objects = {1: "Tom", "2": True, 3: 100.6}
objects = {}
objects = dict()

users_list = [
    ["+111123455", "Tom"],
    ["+384767557", "Bob"],
    ["+958758767", "Alice"]
]
users_dict = dict(users_list)
print(users_dict)

users_tuple = (
    ("+111123455", "Tom"),
    ("+384767557", "Bob"),
    ("+958758767", "Alice")
)
users_dict = dict(users_tuple)
print(users_dict)

users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}

print(users["+11111111"])

key = "+4444444"
if key in users:
    user = users[key]
    print(user)
else:
    print("Элемент не найден")


users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
user1 = users.get("+55555555")
print(user1)

# Removing
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
 
del users["+55555555"] # Removing
user = users.pop(key) # Removing

# Copying dictionares
# Copy to new dict
users = {"+1111111": "Tom", "+3333333": "Bob", "+5555555": "Alice"}
students = users.copy()
print(students)

# Merges to  dicts
users = {"+1111111": "Tom", "+3333333": "Bob"}
 
users2 = {"+2222222": "Sam", "+6666666": "Kate"}
users.update(users2)
 
print(users)
print(users2)

# search
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}
for key in users:
    print(f"Phone: {key}  User: {users[key]} ")
    
for key, value in users.items():
    print(f"Phone: {key}  User: {value} ")

for key in users.keys():
    print(key)

for value in users.values():
    print(value)

# Complex dicts

users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}

old_email = users["Tom"]["email"]
users["Tom"]["email"] = "supertom@gmail.com"
print(users["Tom"])

key = "skype"
if key in users["Tom"]:
    print(users["Tom"]["skype"])
else:
    print("skype is not found")

# Set

users = {"Tom", "Bob", "Alice", "Tom"}
print(users)    # {"Alice", "Bob", "Tom"}

people = ["Mike", "Bill", "Ted"]
users = set(people)
print(users)

users = set()
users.add("Sam")
print(users)

users = {"Tom", "Bob", "Alice"}
 
user = "Tom"
if user in users: 
    users.remove(user)
print(users)


users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
users3 = users.union(users2)
print(users3) # {"Bob", "Alice", "Sam", "Kate", "Tom"}


users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
users3 = users.intersection(users2)
print(users3) # {"Bob"}


users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}
 
users3 = users.symmetric_difference(users2)
print(users3)   # {"Tom", "Alice", "Sam", "Kate"}


users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
 
print(users.issubset(superusers))   # True
print(superusers.issubset(users))   # False


users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
 
print(users.issuperset(superusers))   # False
print(superusers.issuperset(users))   # True

	
users = frozenset({"Tom", "Bob", "Alice"})