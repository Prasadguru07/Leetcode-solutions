# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    # Base case: if the array is empty, return None
    if not nums:
        return None

    # Find the middle element
    mid = len(nums) // 2

    # Create the root node with the middle element
    root = TreeNode(nums[mid])

    # Recursively build the left subtree with the left half of the array
    root.left = sortedArrayToBST(nums[:mid])

    # Recursively build the right subtree with the right half of the array
    root.right = sortedArrayToBST(nums[mid + 1:])

    return root

# Helper function to print the tree in-order (for testing purposes)
def printTree(node):
    if not node:
        return
    printTree(node.left)
    print(node.val, end=' ')
    printTree(node.right)

# Example usage
nums = [10, 2, 3, 4, 5]
nums.sort()  # Ensure the input is sorted
root = sortedArrayToBST(nums)

print("In-order traversal of the constructed BST:")
printTree(root)


# time complexity O(n)
# space complexity O(log n) 