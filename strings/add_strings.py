class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i,j = len(num1) - 1, len(num2) - 1 # validating 2 pointers
        carry = 0
        result = [] # empty list to store values

        while i >= 0 or j >= 0 or carry > 0: # cross validating all three conditions
            digit1 = int(num1[i]) if i >=0 else 0
            digit2 = int(num2[j]) if j >=0 else 0

            total = digit1 + digit2 + carry
            carry = total // 10
            result.append(str(total % 10))

            i -= 1 # verifying outbounds
            j -= 1

        return ''.join(result[::-1]) # reversing the string

# Example usage
num1 = "234"
num2 = "321"
solution = Solution()
result = solution.addStrings(num1, num2)
print(result)  # Output: "555"
