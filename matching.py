def print_hello(language):
    match language:
        case "russian":
            print("Привет")
        case "english" | "american english" | "british english":
            print("Hello")
        case "german":
            print("Hallo")
        case _:
            print("Undefined")
 
 
print_hello("english")      # Hello
print_hello("german")       # Hallo
print_hello("russian")      # Привет
print_hello("spanish")      # Undefined
print_hello("american english")



def operation(a, b, code):
    match code:
        case 1:
            return a + b
        case 2:
            return a - b
        case 3:
            return a * b
        case _:
            return 0
 
 
print(operation(10, 5, 1))      # 15
print(operation(10, 5, 2))      # 5
print(operation(10, 5, 3))      # 50
print(operation(10, 5, 4))      # 0


# Pattern tuples
def print_data(user):
    match user:
        case ("Tom", 37):
            print("default user")
        case ("Tom", age):
            print(f"Age: {age}")
        case (name, 22):
            print(f"Name: {name}")
        case (name, age):
            print(f"Name: {name}  Age: {age}")
 
 
print_data(("Tom", 37))     # default user
print_data(("Tom", 28))     # Age: 28
print_data(("Sam", 22))     # Name: Sam
print_data(("Bob", 41))     # Name: Bob  Age: 41
print_data(("Tom", 33, "Google"))    # не соответствует ни одному из шаблонов


def print_data(user):
    match user:
        case ("Tom", 37):
            print("default user")
        case (name, _):     # второй элемент не важен
            print(f"Name: {name}")
        case (_, _):
            print("Undefined user")
 
 
print_data(("Tom", 37))     # default user
print_data(("Sam", 25))     # Name: Sam
print_data(("Bob", 41))     # Name: Bob


def print_data(user):
    match user:
        case ("Tom", 37, *rest):
            print(f"Rest: {rest}")
        case (name, age, *rest):
            print(f"{name} ({age}): {rest}")
 
 
print_data(("Tom", 37))               # Rest: []
print_data(("Tom", 37, "Google"))     # Rest: ["Google"]
print_data(("Bob", 41, "Microsoft", "english"))     # Bob (41): ["Microsoft", "english"]

# Pattern lists

def print_people(people):
    match people:
        case ["Tom", "Sam", "Bob"]:
            print("default people")
        case ["Tom", second, _]:
            print(f"Second Person: {second}")
        case [first, second, third]:
            print(f"{first}, {second}, {third}")
 
list = ["Tom", "Mike", "Bob"]
print_people(list)
print_people(["Tom", "Sam", "Bob"])         # default people
print_people(["Tom", "Mike", "Bob"])        # Second Person: Mike
print_people(["Alice", "Bill", "Kate"])     # Alice, Bill, Kate
print_people(["Tom", "Kate"])               # несоответствует ни одному из шаблонов



def print_people(people):
    match people:
        case [_]:
            print("Массив из одного элемента")
        case [_, _]:
            print("Массив из двух элементов")
        case [_, _, _]:
            print("Массив из трех элементов")
        case _:
            print("Непонятно")
 
 
print_people(["Tom"])                   # Массив из одного элемента
print_people(["Tom", "Sam"])            # Массив из двух элементов
print_people(["Tom", "Sam", "Bob"])     # Массив из трех элементов
print_people("Tom")                     # Непонятно


def print_people(people):
    match people:
        case [first, *other]:
            print(f"First: {first}  Other: {other}")
 
 
print_people(["Tom"])                   # First: Tom  Other: []
print_people(["Tom", "Sam"])            # First: Tom  Other: ["Sam"]
print_people(["Tom", "Sam", "Bob"])     # First: Tom  Other: ["Sam", "Bob"]


def print_people(people):
    match people:
        case [first, *_]:
            print(f"First: {first}")
 
 
print_people(["Tom"])                   # First: Tom
print_people(["Sam", "Tom"])            # First: Sam
print_people(["Bob", "Sam", "Tom"])     # First: Bob


# Classes patterns

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def print_person(person):
    match person:
        case Person(name="Tom", age=27):
            print("Default person")
        case Person(name=name, age=27):
            print(f"Name: {name}")
        case Person(name=name, age=age):
            print(f"Name: {name} \t age: {age}")

print_person(Person("Ilia", 29))
print_person(Person("Tom", 27))