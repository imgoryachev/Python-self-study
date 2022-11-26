# class 
class Person:
# method (function)
    def say(self, message):
        print(message)
# second method
    def say_hello(self):
        self.say("Hello gays")

    def say_Diman_loh(self):
        self.say("Diman loh")

# definition object from class
tom = Person()
# definition method from class
tom.say_hello()
tom.say_Diman_loh()


class Simple:
    # Class constructor
    def __init__(self):
        print("Create Python object")

    def say_hi(self):
        print("Hi")

one = Simple()

one.say_hi()


# Class with attributes

class Atri:
    def __init__(self,name):
        self.name = name
        self.age = 1

    def display_info(self):
        print(f"{self.name}\t{self.age}")

exec = Atri("Diman")

print(exec.name)
print(exec.age)

exec.name = 30
print(exec.name)

# New attribute
exec.color = "Red"
print(exec.color)

exec.display_info()

# Encapsulation

class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

# Properties manually

    def set_age(self, age):
        if 1 < age < 90:
            self.__age = age
        else:
            print("Invalid value age")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def get_info(self):
        print(f"Name: {self.__name}\tage: {self.__age}")

Diman = Person("Dima")
Diman.set_age(200)
Diman.get_info()



class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1

# Properties by using annotations 

    @property # accessor or getter
    def age(self):
        return self.__age

    @age.setter # mutator or setter
    def age(self, age):
        if 1 < age < 90:
            self.__age = age
        else:
            print("Invalid value age")

    @property
    def get_name(self):
        return self.__name

    def get_info(self):
        print(f"Name: {self.__name}\tage: {self.__age}")

dima = Person("Diman")

dima.get_info()
dima.age = 30
dima.get_info()

# Inheritance

class Person: # Base class or Parent class
    
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def get_info(self):
        return print(f"Name is {self.name} ")

class Employee(Person): # Derived class or Child class
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company
    
    def get_info(self):
        super().get_info()
        print(f"Company: {self.company}")

    def work(self):
        print(f"{self.name} works")

diman = Employee("Dmitry", "EPAM")
diman.get_info()

# Check objects type

class Person:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    def do_nothing(self):
        print(f"{self.name} do nothing")

class Employee(Person):

    def work(self):
        print(f"{self.name} works")

class Student(Person):

    def study(self):
        print(f"{self.name} studies")

def act(person):
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Employee):
        person.work()
    elif isinstance(person, Person):
        person.do_nothing()

tom = Employee("Tom")
bob = Student("Bob")
sam = Person("Sam")

act(tom)
act(bob)
act(sam)

# Class type

class Person:
    type = "Person"
    description = "This is a person"

tom = Person()
print(tom.type)


class Person:
    name = "Undefined"

    def print_name(self):
        print(self.name)

tom = Person()
bob = Person()

tom.print_name()
bob.print_name()

bob.name = "Bob"
tom.print_name()
bob.print_name()

class Person:
    __type = "Person"

    @staticmethod
    def print_type():
        print(Person.__type)

Person.print_type()

tom = Person()
tom.print_type()

# String representation of the class

class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def display_info(self):
        print(self)
        #print(f"Name is {self.name}, age is {self.age}")

    def __str__(self) -> str:
        return f"Name is {self.name}, age is {self.age}"

tom = Person("tom", 23)
print(tom)