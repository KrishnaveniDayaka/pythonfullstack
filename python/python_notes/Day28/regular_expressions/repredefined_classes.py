import re
text = "Python_123 @ Code!"
result1 = re.findall(r'\s', text) # 1. \s → Whitespace characters
print("Whitespace:", result1)
result2 = re.findall(r'\S', text)# 2. \S → Non-whitespace characters
print("Non-whitespace:", result2)
result3 = re.findall(r'\d', text) # 3. \d → Digits
print("Digits:", result3)
result4 = re.findall(r'\D', text) # 4. \D → Non-digits
print("Non-digits:", result4)
result5 = re.findall(r'\w', text)  # 5. \w → Word characters
print("Word characters:", result5) 
result6 = re.findall(r'\W', text)  # 6. \W → Non-word characters
print("Non-word characters:", result6)
result7 = re.findall(r'.', text) # 7. . → Any character except newline
print("Any characters:", result7)