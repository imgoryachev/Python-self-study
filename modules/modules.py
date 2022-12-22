# default modules

# random()

import random

number = random.random() * 100
print(number)

# randint()

number1 = random.randint(20, 35)
print(number1)

# randrange()

number = random.randrange(10)  # значение от 0 до 10 не включая
print(number)
number = random.randrange(2, 10)  # значение в диапазоне 2, 3, 4, 5, 6, 7, 8, 9
print(number)
number = random.randrange(2, 10, 2)  # значение в диапазоне 2, 4, 6, 8
print(number)

# shuffle() and choise()

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)  

random_number = random.choice(numbers)
print(random_number)

# math()

"""
pow(num, power): возведение числа num в степень power

sqrt(num): квадратный корень числа num

ceil(num): округление числа до ближайшего наибольшего целого

floor(num): округление числа до ближайшего наименьшего целого

factorial(num): факториал числа

degrees(rad): перевод из радиан в градусы

radians(grad): перевод из градусов в радианы

cos(rad): косинус угла в радианах

sin(rad): синус угла в радианах

tan(rad): тангенс угла в радианах

acos(rad): арккосинус угла в радианах

asin(rad): арксинус угла в радианах

atan(rad): арктангенс угла в радианах

log(n, base): логарифм числа n по основанию base

log10(n): десятичный логарифм числа n
"""

import random
import math
n1 = math.pow(2, 4)
# n1 = 2**3
print(n1)

n2 = random.random() * 100
print(math.ceil(n2))
print(math.floor(n2))

# locale
# Formatting numbers(time, money, etc) to desired region
# deutch
import locale
locale.setlocale(locale.LC_ALL, "de")        # для  Windows
# locale.setlocale(locale.LC_ALL, "de_DE")   # для MacOS
 
number = 12345.6789
formatted = locale.format_string("%f", number)
print(formatted)    # 12345,678900
 
formatted = locale.format_string("%.2f", number)
print(formatted)    # 12345,68
 
formatted = locale.format_string("%d", number)
print(formatted)    # 12345
 
formatted = locale.format_string("%e", number)
print(formatted)    # 1,234568e+04
 
money = 234.678
formatted = locale.currency(money)
print(formatted)    # 234,68 €


# decimal

from decimal import Decimal
 
number = Decimal("0.1")
number = number + number + number
print(number)

from decimal import Decimal
 
number = Decimal("0.444")
number = number.quantize(Decimal("1.00"))
print(number)       # 0.44
 
number = Decimal("0.555678")
print(number.quantize(Decimal("1.00")))       # 0.56
 
number = Decimal("0.999")
print(number.quantize(Decimal("1.00")))       # 1.00


# Dataclasses
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int = 18

tom = Person("Tom", 38)
print(f"Name: {tom.name}  Age: {tom.age}")

# default dataclass parameters
# def dataclass(cls=None, /, *, init=True, repr=True, eq=True, order=False,
#               unsafe_hash=False, frozen=False, match_args=True,
#               kw_only=False, slots=False)
from dataclasses import dataclass
 
@dataclass(unsafe_hash=True, order=True)
class Person:
    name: str
    age: int
    def __repr__(self):
        return f"Person. Name: {self.name}  Age: {self.age}"
 
 
tom = Person("Tom", 38)
print(tom.__hash__())   # 568439084133251815
print(tom)              # Person. Name: Tom  Age: 38

from dataclasses import dataclass
 
@dataclass
class Person:
    name: str
    age: int
 
    def say_hello(self):
        print(f"{self.name} says hello")
 
 
tom = Person("Tom", 38)
tom.say_hello()


# platform
# check current OC
import platform
platform.system()

from sys import platform
if platform == "linux" or platform == "linux2":
    print("linux")
elif platform == "darwin":
    print("OS X")
elif platform == "win32":
    print("Windows")