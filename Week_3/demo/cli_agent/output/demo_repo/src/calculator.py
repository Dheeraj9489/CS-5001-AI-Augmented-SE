"""A simple calculator module with basic arithmetic operations."""

def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Sum of a and b.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Difference of a and b (a - b).
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        Product of a and b.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    Args:
        a: Dividend.
        b: Divisor.

    Returns:
        Quotient of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
