def search(nums, target):
    low,high = 0, len(nums) - 1

    while low <= high - 1 :
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid -1

    return low

nums = [1,2,3,4,5]
target = [3]
k = search(nums,target)
print(k)