import random
import time
def quick_sort(arr,low,high):
    if(low<high):
        part_indx=partition(arr,low,high)
        quick_sort(arr,low,part_indx-1)
        quick_sort(arr,part_indx+1,high)
def partition(arr,low,high):
    pivot=arr[low]
    i=low+1
    j=high
    while True:
        while(i<=j) and arr[i]<=pivot:
            i=i+1
        while(i<=j) and arr[j]>pivot:
            j=j-1
        if i<=j:
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
    arr[low],arr[j]=arr[j],arr[low]
    return j
arr=random.sample(range(1,20),10) 
print('average case')
start=time.time()
quick_sort(arr,0,len(arr)-1)
print(arr)
end=time.time()
print(end-start)
arr1=random.sample(range(1,20),10) 
print('best case')
arr1.sort()
#print(arr1)
start=time.time()
quick_sort(arr1,0,len(arr1)-1)
end=time.time()
print(end-start)
arr2=random.sample(range(1,20),10) 
print('worst case')
arr2.sort(reverse=True)
#print(arr2)
start=time.time()
quick_sort(arr2,0,len(arr2)-1)
end=time.time()
print(end-start)

