def safe_divide(numerator, denominator):
    try:
        division = float(numerator) / float(denominator)
        return f"The result of the division is {division:.1f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."