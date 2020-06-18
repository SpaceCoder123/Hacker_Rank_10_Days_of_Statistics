from statistics import median
x=int(input())
X=list(map(int,input().split()))
X.sort()
print(round(median(X[:5])))
print(round(median(X)))
print(round(median(X[-5:])))
