def safe_divide(numerator, denominator) -> float:
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom != 0:
            result = num / denom
            print(f"The result of the division is {result}")
            return result
        else:
            print("Error: Cannot divide by zero.")
            return None
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None
