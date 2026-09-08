import re
text = "Python123 @Code2026! Hello"
result1 = re.findall(r'[abc]', text) # 1. Match a, b, or c
print("a, b, c:", result1)
result2 = re.findall(r'[0-9]', text) # 2. Match digits from 0 to 9
print("Digits:", result2)
result3 = re.findall(r'[a-z]', text) # 3. Match lowercase letters
print("Lowercase letters:", result3)
result4 = re.findall(r'[A-Z]', text) # 4. Match uppercase letters
print("Uppercase letters:", result4)
result5 = re.findall(r'[a-zA-Z]', text) # 5. Match all alphabets
print("All alphabets:", result5)
result6 = re.findall(r'[a-zA-Z0-9]', text) # 6. Match alphabets and digits
print("Alphabets and digits:", result6)
result7 = re.findall(r'[^a-zA-Z0-9]', text) # 7. Match special characters
print("Special characters:", result7)