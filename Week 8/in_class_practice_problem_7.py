while(True):
    try:
        #Get first number
        a = input("Please enter the first number: ")
        if (a == "q"):
            break
        a = int(a)
        #Get second number
        b = input("Please enter the second number: ")
        if (b == "q"):
            break
        b = int(b)
        #Get operator
        operator = input("Please enter the operator (+, -, *, /): ")
        if (operator == "q"):
            break
        if operator not in ["+", "-", "*", "/"]:
            raise Exception
        if (b == 0 and operator == "/"):
            raise ZeroDivisionError
    except ValueError:
        print("Your input cannot be converted to an integer.")
    except ZeroDivisionError:
        print("You cannot divide by zero.")
    except Exception:
        print("You have entered an invalid operator.")
    else:
        if operator == "+":
            print(f"{a}+{b}={a+b}")
        elif operator == "-":
            print(f"{a}-{b}={a-b}")
        elif operator == "*":
            print(f"{a}*{b}={a*b}")
        elif operator == "/":
            print(f"{a}/{b}={a/b}")
    finally:
        print("Attempt complete.\n")