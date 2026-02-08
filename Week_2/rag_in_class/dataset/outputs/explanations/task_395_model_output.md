# Model output for task_395

## Model
- devstral-small-2:24b-cloud

## Original Code:

def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

## Refactored Code:

```python
def first_non_repeating_character(str1):
    char_order = []
    ctr = {}
    for c in str1:
        if c in ctr:
            ctr[c] += 1
        else:
            ctr[c] = 1
            char_order.append(c)
    for c in char_order:
        if ctr[c] == 1:
            return c
    return None
```

- Preserved the exact function name and variable names as required
- Maintained the original logic for tracking character order and counts
- Kept the same return behavior (returns None when no non-repeating character exists)
- Ensured the function processes characters in their original order
- Used the same dictionary and list data structures as the original
- Preserved the two-pass approach (first to count, second to check)
- Maintained the same edge case handling (returns None for no matches)
- Kept the exact same return types (character or None)
- No additional functionality or changes were made
- All test cases should pass exactly as before
