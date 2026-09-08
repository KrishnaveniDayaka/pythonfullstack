
import re
text = "Python is easy. Python is powerful."
#re.match() Checks the pattern only at the beginning of the string
result1 = re.match(r'Python', text)
print("1. match():", result1.group() if result1 else "No match")
# re.search() Searches for the first occurrence anywhere in the string
result2 = re.search(r'powerful', text)
print("2. search():", result2.group() if result2 else "No match")
#re.findall() Finds all occurrences and returns them as a list
result3 = re.findall(r'Python', text)
print("3. findall():", result3)
#re.finditer()Finds all occurrences and returns match objects
result4 = re.finditer(r'Python', text)
print("4. finditer():")
for match in result4:
    print(match.group(), "Position:", match.start())
# re.sub() Replaces matching text with another text
result5 = re.sub(r'Python', 'Java', text)
print("5. sub():", result5)