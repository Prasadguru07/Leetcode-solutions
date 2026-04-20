text = "HelloWorld"

for index, letter in enumerate(text):
    if index % 2 == 0:
        print(letter, end="") 
        
# Output: Hlool


text = "ExampleString"
# Starts at 1, goes to the end, steps by 2
even_letters = text[1::2] 
print(even_letters) # Output: EamlSrn