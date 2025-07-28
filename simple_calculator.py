def basic_calculator(num1, num2, operator):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="/":
        if num2==0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1/num2
    else:
        return "Invalid operator. Please try again!"

if __name__=="__main__":
    try:
        num1=int(input("Enter the first number: "))
        num2=int(input("Enter the second number: "))
        operator=input("Enter the operator (+, - ,*, / ): ")
        result=basic_calculator(num1, num2, operator)
        print(f"The result of {num1} {operator} {num2 } is {result}.")
    except Exception as e:
        print(f"An error occurred:{e}")

