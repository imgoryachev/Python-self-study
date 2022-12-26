text = "Message:\n\"Hello World\""
print(text)

# r for denied spec symbols
path = r"C:\python\name.txt"
print(path)

# f for use variables in var
userName = "Tom"
userAge = 37
user = f"name: {userName}  age: {userAge}"
print(user)   # name: Tom  age: 37


string = "hello world"
for char in string:
    print(char)


string = "hello world"
 
# с 0 до 5 индекса
sub_string1 = string[:5]
print(sub_string1)      # hello
 
# со 2 до 5 индекса
sub_string2 = string[2:5]
print(sub_string2)      # llo
 
# с 2 по 9 индекса через один символ
sub_string3 = string[2:9:2]
print(sub_string3)      # lowr



name = "Tom"
surname = "Smith"
fullname = name + " " + surname
print(fullname)

name = "Tom"
age = 33
info = "Name: " + name + " Age: " + str(age)
print(info)


# search in string
string = "hello world"
exist = "hello" in string
print(exist)

welcome = "Hello world! Goodbye world!"
index = welcome.find("wor")
print(index)       # 6
 
# поиск с 10-го индекса
index = welcome.find("wor",10)
print(index)       # 21
 
# поиск с 10 по 15 индекс
index = welcome.find("wor",10,15)
print(index)       # -1


phone = "+1-234-567-89-10"
 
# замена дефисов на пробел
edited_phone = phone.replace("-", " ")
print(edited_phone)     # +1 234 567 89 10
 
# удаление дефисов
edited_phone = phone.replace("-", "")
print(edited_phone)     # +12345678910
 
# замена только первого дефиса
edited_phone = phone.replace("-", "", 1)
print(edited_phone)     # +1234-567-89-10


file_name = "hello.py"
 
starts_with_hello = file_name.startswith("hello")   # True
ends_with_exe = file_name.endswith("exe")           # False


print("iPhone 7:", "52000".rjust(10))
print("Huawei P10:", "36000".rjust(10))


# splitting
text = "Это был огромный, в два обхвата дуб, с обломанными ветвями и с обломанной корой"
# разделение по пробелам
splitted_text = text.split()
print(splitted_text)
print(splitted_text[6])     # дуб,
 
# разбиение по запятым
splitted_text = text.split(",")
print(splitted_text)
print(splitted_text[1])     # в два обхвата дуб
 
# разбиение по первым пяти пробелам
splitted_text = text.split(" ", 5)
print(splitted_text)        
print(splitted_text[5])     # обхвата дуб, с обломанными ветвями и с обломанной корой



words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]
 
# разделитель - пробел
sentence = " ".join(words)
print(sentence)  # Let me speak from my heart in English


# Formatting
text = "Hello, {first_name}.".format(first_name="Tom")
print(text)     # Hello, Tom.
 
info = "Name: {name}\t Age: {age}".format(name="Bob", age=23)
print(info)     # Name: Bob  Age: 23


info = "Name: {0}\t Age: {1}".format("Bob", 23)
print(info)     # Name: Bob  Age: 23


info = "Имя: %s \t Возраст: %d" % ("Tom", 35)
print(info)   # Имя: Tom     Возраст: 35

number = 23.8589578
print("%0.2f  - %e" % (number, number))   # 23.86  - 2.385896e+01