#Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
n=int(input())
arr=list(map(int,input().split()))
se=-1
for i in range(n):
    count=0
    for j in range(n):
        if arr[i]==arr[j]:
            count+=1
    if count==1:
        se=arr[i]
        break
print(se)