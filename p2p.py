#Problem Statement: Given an integer array nums, rotate the array to the left by one.

n=int(input())
arr=list(map(int,input().split()))
temp=arr[0]
for i in range(1,n):
    arr[i-1]=arr[i]
arr[n-1]=temp
for x in arr:
    print(x,end=" ")