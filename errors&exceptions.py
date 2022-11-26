# Error processing
# Exist two error types: 
# . syntax errors 
# . runtime errors

try:
    number = int(input("Enter number: "))
    print("Entered number:", number)
except:
    print("Converting was unsuccessfully")
finally:
    print("This sentence will be anyway because of \"finally\"")
print("End of program")




try:
    number = int(input("Enter number: "))
    print("Entered number:", number)
except ValueError:
    print("Преобразование прошло неудачно")
print("Завершение программы")



try:
    number = int(input("Enter number: "))
    print("Entered number:", number)
except ValueError as e:
    print("Exception information", e)
print("End of program")