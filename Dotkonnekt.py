def Dup(arr):
    
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

arr = [1, 2, 3, 4, 5, 2, 3]
print(Dup(arr))