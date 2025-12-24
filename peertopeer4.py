#Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements.
# Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

n=int(input())
arr=list(map(int,input().split()))
pos=[]
neg=[]
for x in arr:
    if x>0:
        pos.append(x)
    else:
        neg.append(x)
result=[]
i=0
while i<len(pos):
    result.append(pos[i])
    result.append(neg[i])
    i+=1
print(result)