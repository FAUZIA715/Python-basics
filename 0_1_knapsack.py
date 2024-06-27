def knap(w,wt,value,n):
    k=[[0 for j in range(w+1)]for i in range (n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0:
                    k[i][j]=0
            elif wt[i-1]<=j:
                 k[i][j]=max(value[i-1]+k[i-1][j-wt[i-1]],k[i-1][j])
            else:
                 k[i][j]=k[i-1][j]
    return k[n][j]
if __name__=="__main__":
     profit=[3,4,5,6]
     weight=[2,3,4,5]
     w=5
     n=len(profit)
     x=knap(w,weight,profit,n)
     print(x)