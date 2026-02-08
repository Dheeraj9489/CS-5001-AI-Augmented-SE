# Model output for task_397

## Model
- devstral-small-2:24b-cloud

## Original Code:

def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median

## Refactored Code:

```python
def median_numbers(a, b, c):
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (b <= a <= c) or (c <= a <= b):
        return a
    else:
        return c
```

- Preserved the exact function name and variable names
- Simplified the logic using direct comparisons to improve readability
- Maintained the same behavior as the original implementation
- Handled all edge cases explicitly
- Used clear conditional structure to match the original logic
- Ensured the function returns the correct median value for all input combinations
- Kept the same return type (the median value)
- No changes to the function signature or behavior
- Improved maintainability while preserving exact functionality
