# Model output for task_392

## Model
- devstral-small-2:24b-cloud

## Original Code:

def get_max_sum (n):
	res = list()
	res.append(0)
	res.append(1)
	i = 2
	while i<n + 1:
		res.append(max(i, (res[int(i / 2)] 
						+ res[int(i / 3)] +
							res[int(i / 4)]
						+ res[int(i / 5)])))
		i = i + 1
	return res[n]

## Refactored Code:

```python
def get_max_sum(n):
    res = [0, 1]
    for i in range(2, n + 1):
        res.append(max(i, res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5]))
    return res[n]
```

- Preserved the exact function name and variable names
- Simplified the loop structure while maintaining identical behavior
- Used integer division (//) consistently for clarity
- Maintained the same initialization and logic flow
- Ensured the return value matches the original implementation exactly
- Kept the same edge case handling (returns 0 for n=0, 1 for n=1)
- Preserved the exact mathematical formula from the original
- Maintained the same list indexing approach
- No changes to the core algorithm or logic
- All test cases should pass with identical results
