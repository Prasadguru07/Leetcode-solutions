def plusone(digits):
    for i in range(len(digits) -1,-1,-1): # -1 for last digit and -1 for right to left traversal
        if digits[i] < 9: 
           digits[i] += 1# no carry add +1 to number
           return digits
        digits[i] = 0 # if carry present +1 to digits and return digits 
    return[1] + digits

digits = [1,2,3,4] # calling the function
pl = plusone(digits)
print(pl)

# time complexity O(1)
# space complxity O(1)