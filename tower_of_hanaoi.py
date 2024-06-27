import time
def TOH( n, A, B, C):
    if(n>0):
        TOH(n-1,A,C,B)
        print("move a disc from ",A," to ",C)
        TOH(n-1,B,A,C)
n=int(input("enter the total number of disc"))
start=time.time()
TOH(n,'A','B','C')
end=time.time()
print(end-start)