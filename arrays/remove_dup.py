def rem_dup(nums):
    if not nums:  # Handle edge case for empty array
        return 0

    i = 0  # Pointer for the last unique element
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:  # Check if current element is unique
            i += 1  # Move unique pointer
            nums[i] = nums[j]  # Update the position with the unique element
    return i + 1  # Number of unique elements

nums = [1, 1, 2]
k = rem_dup(nums)  # Call the function
print(k)  # Output the number of unique elements
print(nums[:k])  # Print the unique elements in the modified array
