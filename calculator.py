#calculator

print("Select an operation to perform: ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Divide")
print("Enter number(1-4) to perform operation: ")

operation = input()

#code for addition
if operation == "1":
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")
    print("The sum is: " + str(int(number1) + int(number2)))
#code for subtraction
elif operation == "2":
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")
    print("The difference is: " + str(int(number1) - int(number2)))
# code for multiplication
elif operation == "3":
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")
    print("The product is: " + str(int(number1) * int(number2)))
# code for division
elif operation == "4":
    number1 = input("Enter first number: ")
    number2 = input("Enter second number: ")
    print("The result is: " + str(int(number1) / int(number2)))
else:
    print("Invalid Entry")