# Model output for task_558

## Model
- devstral-small-2:24b-cloud

## Original Code:

def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))

## Refactored Code:

```python
def digit_distance_nums(n1, n2):
    distance = abs(n1 - n2)
    return sum(int(digit) for digit in str(distance))
```

- Preserved the exact function name and variable names
- Improved readability by using a generator expression instead of map
- Maintained the same behavior for all inputs
- Kept the same mathematical operation (absolute difference)
- Ensured the return type remains an integer sum of digits
- Handled edge cases implicitly through the existing logic
- No changes to the core calculation formula
- Maintained the same input/output contract
- Used more Pythonic iteration over string digits
- Preserved the exact behavior for all test cases
