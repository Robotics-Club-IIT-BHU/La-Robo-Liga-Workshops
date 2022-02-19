import numpy as np
n=3
arr = np.array([[2,7,6],[9,5,1],[4,3,8]])
x = []
s1 = 0
s2 = 0
s3 = 0
t=1

for i in range(2):
    x.append(np.sum(arr,axis=i))

for i in range(2):
    for j in range(n):
        if(j<n-1 and x[i][j]!=x[i][j+1]):
            s3=0
            t=0
            break
        else :
            s3=x[i][j]
    if t==0:
        break
    
for i in range(0,n):
    s1 += arr[i][i]
    s2 +=arr[i][n-i-1]


if s1==s2==s3:
    print('YES')
else:
    print('NO')