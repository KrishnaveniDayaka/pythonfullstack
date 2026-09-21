
n=list(map(int,input("enter numbers:").split()))
target=int(input("Enter target element:"))
found=False
for i in range(len(n)):
  if n[i]==target:
    found=True
    break
if found:
  print("Element found")
else:
  print("Element not found")