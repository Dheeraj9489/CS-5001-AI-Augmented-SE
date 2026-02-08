import cmath

def convert(numbers):
    num = cmath.polar(numbers)
    real_part, imaginary_part = num
    return (float(real_part), float(imaginary_part))
