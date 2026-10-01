
def quick_sort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    i+=1
    arr[i],arr[high]=arr[high],arr[i]
    return i
arr=[10,2,13,7]
quick_sort(arr,0,len(arr)-1)
print(arr)