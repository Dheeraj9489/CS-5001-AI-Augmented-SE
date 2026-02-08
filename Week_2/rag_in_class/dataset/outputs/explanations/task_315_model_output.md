# Model output for task_315

## Model
- devstral-small-2:24b-cloud

## Original Code:

def find_Max_Len_Even(str): 
    n = len(str) 
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while (i < n): 
        if (str[i] == ' '): 
            if (currlen % 2 == 0): 
                if (maxlen < currlen): 
                    maxlen = currlen 
                    st = i - currlen 
            currlen = 0 
        else : 
            currlen += 1
        i += 1
    if (currlen % 2 == 0): 
        if (maxlen < currlen): 
            maxlen = currlen 
            st = i - currlen 
    if (st == -1): 
        return "-1" 
    return str[st: st + maxlen] 

## Refactored Code:

```python
def find_Max_Len_Even(str):
    n = len(str)
    i = 0
    currlen = 0
    maxlen = 0
    st = -1
    while i < n:
        if str[i] == ' ':
            if currlen % 2 == 0:
                if maxlen < currlen:
                    maxlen = currlen
                    st = i - currlen
            currlen = 0
        else:
            currlen += 1
        i += 1
    if currlen % 2 == 0:
        if maxlen < currlen:
            maxlen = currlen
            st = i - currlen
    if st == -1:
        return "-1"
    return str[st:st + maxlen]
```

- Maintained the exact function name and variable names as specified
- Preserved the original logic and behavior to pass all test cases
- Improved readability with consistent indentation and spacing
- Kept the same return type handling (string "-1" for no match)
- Maintained the original edge case handling (st == -1)
- Preserved the exact same control flow and conditions
- No changes to the core algorithm or logic
- All variable names remain unchanged
- The function signature remains identical
- The return value format is exactly as in the original
