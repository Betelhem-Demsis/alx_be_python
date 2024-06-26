number1= int(input("Enter the first number: "))
number2= int(input("Enter the Second number: "))
operations= input("Choose the operation (+, -, *, /): ")
match operations:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "*":
        result = number1 * number2
    case "/":
        result = number1 / number2
        if (number2==0):
            print("can't divide a number by zero")
    case _:
        print("choose operations ")
print("The result is", result)