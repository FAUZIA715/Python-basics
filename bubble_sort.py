import time
import random
def bubble_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range (0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return -1
print("average")
mylist=random.sample(range(1,2000),10)
#print(mylist)
start=time.time()
bubble_sort(mylist)
print(mylist)