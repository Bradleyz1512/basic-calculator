
# Prompts user for 2 numbers and an operator
num1 = input("Number: ")
operator = input("Add, subtract, multiply or divide? (+, -, *, /): ")
num2 = input("By?: ")

# Converts user input to float
num1 = float(num1)
num2 = float(num2)

# Solves for chosen operator
if operator == ("+"):
    print("Answer =", num1 + num2)
elif operator == ("-"):
    print("Answer =", num1 - num2)
elif operator == ("*"):
    print("Answer =", num1 * num2)
elif operator ==("/"):
    if num2 == 0:
        print("Cannot divide by 0!")
    else:
        print("Answer =", num1 / num2)

else:
    print("ERROR: invalid operator input")    