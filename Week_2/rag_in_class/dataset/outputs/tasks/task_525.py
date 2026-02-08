def parallel_lines(line1, line2):
    # Check if lines are parallel by comparing their slopes
    # Handle division by zero cases by returning False
    try:
        slope1 = line1[0] / line1[1]
    except ZeroDivisionError:
        return False

    try:
        slope2 = line2[0] / line2[1]
    except ZeroDivisionError:
        return False

    return slope1 == slope2
