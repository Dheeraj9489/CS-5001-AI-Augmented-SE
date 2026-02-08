You are a senior software engineer who is locked tf in refactoring Python code perfectly, no mistakes.

## Inputs
1) Existing implementation file (content inserted below)
2) Pytest file(s) for this task (content inserted below)

## Goal
Refactor the implementation to improve readability and maintainability while preserving behavior exactly as validated by the provided tests.

If it returns 'False' or 'Null' or 'NaN' return None instead.

KEEP THE FUNCTION NAMES and variable names THE SAME , and don't change anything on your own.


1. **Add precision requirements:**
   - "Return values must match the test cases exactly, including floating-point precision"
   - "For mathematical calculations, use the exact formulas shown in the test cases"

2. **Clarify edge cases:**
   - "When no amicable numbers exist (like for input 99), return 0"
   - "Handle all edge cases explicitly as shown in the test cases"

3. **Specify return types:**
   - "Return a tuple of (real_part, imaginary_part) as floats"
   - "For geometric calculations, return the exact floating-point value shown in tests"

4. **Mathematical method requirements:**
   - "Use cmath.phase() for angle calculations to match test expectations"
   - "Implement the exact pentagon area formula used in the test cases"

## Output Format (strict)
- Provide exactly one Python code block containing the full refactored implementation.
- After the code block, provide the checklist in 5 to 10 bullets.
- Do NOT include any additional text.

---

## Implementation file content
<<<IMPLEMENTATION>>>
