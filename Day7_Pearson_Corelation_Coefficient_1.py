import math
def find_mean(A):
    return (sum(A)/len(A))
 
def standard_deviation(A,Mean):
    # Standard Deviation
    Std=[]
    for i in A:
        Std.append((i-Mean)**2)
    return (math.sqrt(sum(Std)/len(A)))

def pearson_correlation_coefficient(X,Std_of_X,mean_X,Y,Std_of_Y,mean_Y,n):
    summation=[]
    for x,y in zip(X,Y):
        summation.append((x-mean_X)*(y-mean_Y))
    return sum(summation)/(n*Std_of_X*Std_of_Y)



n=int(input())
X=list(map(float,input().split()))
Y=list(map(float,input().split()))
MX,MY=find_mean(X),find_mean(Y)
StdX,StdY=standard_deviation(X,MX),standard_deviation(Y,MY)
print('{0:.3f}'.format(pearson_correlation_coefficient(X,StdX,MX,Y,StdY,MY,n)))
