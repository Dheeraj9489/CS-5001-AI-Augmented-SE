# Model output for task_123

## Model
- devstral-small-2:24b-cloud

## Original Code:

def amicable_numbers_sum(limit):
    if not isinstance(limit, int):
        return "Input is not an integer!"
    if limit < 1:
        return "Input must be bigger than 0!"
    amicables = set()
    for num in range(2, limit+1):
        if num in amicables:
            continue
        sum_fact = sum([fact for fact in range(1, num) if num % fact == 0])
        sum_fact2 = sum([fact for fact in range(1, sum_fact) if sum_fact % fact == 0])
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)
    return sum(amicables)

## Refactored Code:

```python
def amicable_numbers_sum(limit):
    if not isinstance(limit, int):
        return None
    if limit < 1:
        return None
    amicables = set()
    for num in range(2, limit + 1):
        if num in amicables:
            continue
        sum_fact = sum(fact for fact in range(1, num) if num % fact == 0)
        sum_fact2 = sum(fact for fact in range(1, sum_fact) if sum_fact % fact == 0)
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)
    return sum(amicables) if amicables else 0
```

- Preserved all function and variable names exactly as given
- Replaced error strings with `None` as specified
- Added explicit return of `0` when no amicable numbers exist
- Maintained the exact same logic and calculations
- Improved list comprehensions for better readability
- Kept the same set-based approach for tracking amicable numbers
- Ensured the function returns an integer sum as before
- Maintained the same edge case handling (non-integer and negative inputs)
- Preserved the exact same algorithm for finding amicable numbers
