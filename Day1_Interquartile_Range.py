T=int(input())
Element=list(map(int,input().split()))
Frequency=list(map(int,input().split()))
L=[]
k=0
for i in Frequency:
    for j in range(i):
        L.append(Element[k])
    k=k+1
L.sort()
from statistics import median
print('{0:.1f}'.format(abs(median(L[:len(L)//2])-median(L[(len(L)+1)//2:]))))
