import re
text = "Hello Python World! I have a cat, a dog, and aaaa."
result1 = re.search(r'^Hello', text) #  ^ → Check if string starts with "Hello"
print("Starts with Hello:", bool(result1))
result2 = re.search(r'\.$', text)  #  $ → Check if string ends with "."
print("Ends with dot:", bool(result2))
result3 = re.findall(r'a.a', "aba aca a9a") #  . → Any one character
print("Any character between a and a:", result3)
result4 = re.findall(r'ab*', "a ab abb abbb") #  * → Zero or more occurrences
print("Zero or more b:", result4)
result5 = re.findall(r'ab+', "a ab abb abbb") #  + → One or more occurrences
print("One or more b:", result5)
result6 = re.findall(r'ab?', "a ab abb abbb") #  ? → Zero or one occurrence
print("Zero or one b:", result6)
result7 = re.findall(r'ab{2}', "ab abb abbb abbbb") #  {n} → Exactly n occurrences
print("Exactly 2 b:", result7)
result8 = re.findall(r'[aeiou]', "Hello Python") #  [] → Character class
print("Vowels:", result8)
result9 = re.findall(r'cat|dog', text) # | → OR operator
print("Cat or Dog:", result9)
result10 = re.findall(r'(ab)+', "ababab") #  () → Grouping
print("Grouped pattern:", result10)