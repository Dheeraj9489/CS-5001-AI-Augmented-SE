import math
import cmath

def area_pentagon(a):
    """Calculate the area of a regular pentagon with side length a.

    Args:
        a: Side length of the pentagon (float)

    Returns:
        Area of the pentagon as a float, or None for invalid inputs
    """
    if a is None or a is False or (isinstance(a, float) and math.isnan(a)):
        return None

    try:
        area = (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pow(a, 2)) / 4.0
        return area
    except (TypeError, ValueError):
        return None
