
T=int(input())
W=list(map(int,input().split()))
Elements=list(map(int,input().split()))
def wieghted_mean(Value,Key):
    L=[]
    for i,j in zip(Value,Key):
        L.append(i*j)
    return sum(L)/sum(Key)
print('{0:.1f}'.format(wieghted_mean(W,Elements)))
