# Model output for task_107

## Model
- devstral-small-2:24b-cloud

## Original Code:

def count_Hexadecimal(L,R) :  
    count = 0;  
    for i in range(L,R + 1) : 
        if (i >= 10 and i <= 15) : 
            count += 1;  
        elif (i > 15) : 
            k = i;  
            while (k != 0) :  
                if (k % 16 >= 10) : 
                    count += 1;  
                k = k // 16;  
    return count;  

## Refactored Code:

```python
def count_Hexadecimal(L, R):
    count = 0
    for i in range(L, R + 1):
        if 10 <= i <= 15:
            count += 1
        elif i > 15:
            k = i
            while k != 0:
                if k % 16 >= 10:
                    count += 1
                k = k // 16
    return count
```

- Preserved the exact function name and variable names as required
- Improved readability with consistent indentation and spacing
- Maintained the same logic flow and conditions
- Kept the same return value behavior
- Ensured all edge cases are handled as in the original implementation
- Used the same mathematical operations and comparisons
- Maintained the same loop structure and termination conditions
- Preserved the exact same counting mechanism for hexadecimal digits
- Kept the same range handling for the input parameters
- Ensured the function returns the same type (integer) as the original
