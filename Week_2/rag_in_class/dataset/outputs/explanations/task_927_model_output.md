# Model output for task_927

## Model
- devstral-small-2:24b-cloud

## Original Code:

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def max_height(node): 
	if node is None: 
		return 0 ; 
	else : 
		left_height = max_height(node.left) 
		right_height = max_height(node.right) 
		if (left_height > right_height): 
			return left_height+1
		else: 
			return right_height+1

## Refactored Code:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_height(node):
    if node is None:
        return 0
    else:
        left_height = max_height(node.left)
        right_height = max_height(node.right)
        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1
```

- Preserved the exact function name `max_height` and variable names (`node`, `left_height`, `right_height`)
- Maintained the original logic and behavior exactly as in the original implementation
- Kept the same return type (integer) for the height calculation
- Preserved the recursive approach for tree traversal
- Ensured the base case (None node) returns 0 as specified
- Maintained the same comparison logic for determining the maximum height
- No additional functionality or changes were made beyond the original implementation
- The code structure and indentation remain identical to the original
- All edge cases (empty tree, single node, unbalanced tree) are handled as in the original
