def safe_divide(numerator, denominator)->float:
    try:
        num = float(numerator)
        num2= float(denominator)
        if denominator != 0:
           result=num/num2
           print(f"the result of the division is {result}")
           return result
        else:
            print("Error: Cannot divide by zero.")
            return None
    except ValueError:
         print("Error: Please enter numeric values only.")
         return None
