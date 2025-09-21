print("Enter string:")

string = input()
result = ""

for char in string:
    if char not in "aeiou":
        result += char
        
print(result)