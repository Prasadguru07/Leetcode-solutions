name = "Guruprasad"

# ============= BRUTE FORCE METHOD - EVEN INDEXED =============
# Time: O(n), Space: O(n)
# Iterate through each index and check if it's even (0, 2, 4, 6, ...)
def even_letters_brute_force(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:  # Even indices only
            result += s[i]
    return result

# ============= OPTIMAL METHOD - EVEN INDEXED =============
# Time: O(n), Space: O(n)
# Using Python slicing with step - cleaner and slightly faster
def even_letters_optimal(s):
    return s[::2]  # Start:End:Step (step=2 means every 2nd character)

# ============= BONUS - ODD INDEXED LETTERS =============
def odd_letters_optimal(s):
    return s[1::2]  # Start from index 1, step by 2

# Test both methods
print("String:", name)
print("Brute Force:", even_letters_brute_force(name))
print("Optimal Method:", even_letters_optimal(name))

# Additional test cases
test_strings = ["Guruprasad", "LeetCode", "Python", "12345"]
print("\n--- Test Cases ---")
for test in test_strings:
    print(f"'{test}' -> Brute: '{even_letters_brute_force(test)}' | Optimal: '{even_letters_optimal(test)}'")