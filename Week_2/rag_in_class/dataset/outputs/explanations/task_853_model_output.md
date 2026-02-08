# Model output for task_853

## Model
- devstral-small-2:24b-cloud

## Original Code:

import math
def sum_of_odd_Factors(n): 
    res = 1
    while n % 2 == 0: 
        n = n // 2 
    for i in range(3,int(math.sqrt(n) + 1)): 
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0: 
            count+=1 
            n = n // i 
            curr_term *= i 
            curr_sum += curr_term    
        res *= curr_sum  
    if n >= 2: 
        res *= (1 + n) 
    return res 

## Refactored Code:

```python
import math

def sum_of_odd_Factors(n):
    res = 1
    while n % 2 == 0:
        n = n // 2
    for i in range(3, int(math.sqrt(n) + 1)):
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            count += 1
            n = n // i
            curr_term *= i
            curr_sum += curr_term
        res *= curr_sum
    if n >= 2:
        res *= (1 + n)
    return res
```

- Preserved the exact function name and variable names as required
- Maintained the original logic and behavior to pass all test cases
- Kept the mathematical calculations and formulas unchanged
- Ensured the function handles edge cases as per the original implementation
- Used the same data types and return values as the original function
- No additional modifications or optimizations were made beyond readability improvements
- The code structure remains identical to the original implementation
- All mathematical operations and loops are preserved exactly as in the original
- The function signature and return type remain unchanged
- The implementation strictly follows the original behavior for all inputs
