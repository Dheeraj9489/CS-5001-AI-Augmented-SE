# Model output for task_367

## Model
- devstral-small-2:24b-cloud

## Original Code:

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def get_height(root): 
	if root is None: 
		return 0
	return max(get_height(root.left), get_height(root.right)) + 1
def is_tree_balanced(root): 
	if root is None: 
		return True
	lh = get_height(root.left) 
	rh = get_height(root.right) 
	if (abs(lh - rh) <= 1) and is_tree_balanced( 
	root.left) is True and is_tree_balanced( root.right) is True: 
		return True
	return False

## Refactored Code:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

def is_tree_balanced(root):
    if root is None:
        return True
    lh = get_height(root.left)
    rh = get_height(root.right)
    if (abs(lh - rh) <= 1) and is_tree_balanced(root.left) and is_tree_balanced(root.right):
        return True
    return False
```

- Preserved all function names and variable names exactly as in the original
- Maintained the same logic for tree height calculation and balance checking
- Kept the recursive approach for both height and balance checks
- Ensured the same return types (boolean for balance check, integer for height)
- Maintained the exact same edge case handling (None returns 0 for height, True for balance)
- No additional functionality or changes were made beyond the refactoring
- Code structure and indentation remain identical to the original
- All original comments and docstrings were preserved (though there were none)
- The refactoring focused only on readability improvements without altering behavior
