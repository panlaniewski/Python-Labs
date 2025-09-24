string = input("Enter string: ")
# result = ""

# for char in string:
#     if char not in "aeiou":
#         result += char

result = string.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
        
print(result)