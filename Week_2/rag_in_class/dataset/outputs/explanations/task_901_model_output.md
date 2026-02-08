# Model output for task_901

## Model
- devstral-small-2:24b-cloud

## Original Code:

def smallest_multiple(n):
    if (n<=2):
      return n
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i

## Refactored Code:

```python
import math

def smallest_multiple(n):
    if n <= 2:
        return n
    i = n * 2
    factors = [number for number in range(n, 1, -1) if number * 2 > n]
    while True:
        divisible = True
        for a in factors:
            if i % a != 0:
                divisible = False
                i += n
                break
        if divisible:
            return i
```

- Preserved the exact function name and variable names as required
- Improved readability by using a boolean flag `divisible` to track divisibility
- Maintained the same logic flow and mathematical operations
- Kept the same edge case handling for n <= 2
- Preserved the exact same return values and behavior as the original
- Used list comprehension exactly as in the original
- Maintained the same while loop structure and increment logic
- Kept the same factor calculation method
- Ensured the function returns the smallest multiple divisible by all numbers from 1 to n
- All test cases should pass exactly as before with identical output values
