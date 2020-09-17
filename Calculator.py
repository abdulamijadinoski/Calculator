try:
    num1 = float(input("Enter firs number: "))
    op = input("Enter an operator: ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
except ValueError:
    print("Invalid Input!")
