import math 
T=int(input())
X=list(map(int,input().split()))
Squared_Distance=[]
mean=sum(X)/T
for i in range(T):
    Squared_Distance.append((X[i]-mean)**2)

print('{0:.1f}'.format(math.sqrt(sum(Squared_Distance)/T)))
