
n=list(map(int,input("enter numbers:").split()))
target=int(input("Enter target element:"))
found=False
low=0
high=len(n)-1
while low<=high:
  mid=(low+high)//2
  if target==n[mid]:
    found=True
    break
  elif target>n[mid]:
    low=mid+1
  else:
    high=mid-1
if found:
  print("Element found")
else:
  print("Element not found")