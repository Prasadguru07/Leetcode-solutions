from typing import List  # Import List for type hinting

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the next valid position

        # Loop through the array
        for i in range(len(nums)):
            # Check if the current element is not equal to val
            if nums[i] != val:
                nums[k] = nums[i]  # Move the valid element to the position k
                k += 1  # Increment k

        return k  # Return the count of valid elements

# Test the solution
nums = [3, 2, 2, 3]
val = 3
solution = Solution()
k = solution.removeElement(nums, val)

# Output the result
print(f"Number of elements after removal: {k}")
print(f"Modified array: {nums[:k]}")
