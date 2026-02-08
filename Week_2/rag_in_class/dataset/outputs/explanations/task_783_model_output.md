# Model output for task_783

## Model
- devstral-small-2:24b-cloud

## Original Code:

def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v

## Refactored Code:

```python
import math

def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn

    if mx == mn:
        h = 0.0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360

    if mx == 0:
        s = 0.0
    else:
        s = (df / mx) * 100.0

    v = mx * 100.0

    return (h, s, v)
```

- Preserved all function and variable names exactly as in the original
- Maintained the exact same logic and calculations for HSV conversion
- Ensured floating-point precision by explicitly using .0 for all numeric values
- Kept the same return format (tuple of floats)
- Handled all edge cases (mx == mn, mx == 0) exactly as in the original
- Used the same mathematical formulas for hue, saturation, and value calculations
- No additional functionality or changes were made beyond the refactoring for clarity
