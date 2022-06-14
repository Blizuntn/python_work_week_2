def add(n1, n2):
    print(n1 + n2)


def subtract(n1, n2):
    print(n1 - n2)


def multiply(n1, n2):
    print(n1 * n2)


def divide(n1, n2):
    print(n1 / n2)


is_on = True

while is_on:

    proceed = input(
        "Would you like to proceed with the calculator? yes or no: ")
    if proceed == "no":
        break
    calculation = input(
        "What kind of calculation would you like to perform? add subtract multiplication division:  ").lower()
    number1 = int(input("What is your first number? "))
    number2 = int(input("What is your second number? "))

    if calculation == "add":
        add(number1, number2)
    elif calculation == "subtract":
        subtract(number1, number2)
    elif calculation == "multiplication":
        multiply(number1, number2)
    elif calculation == "division":
        divide(number1, number2)
