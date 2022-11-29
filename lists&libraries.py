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