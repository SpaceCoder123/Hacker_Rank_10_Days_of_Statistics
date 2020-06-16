from scipy import stats
def mean_of_array(A):
    return sum(A)/len(A)

def median_of_array(A):
    A.sort()
    # print(A)
    return (A[len(A)//2]+A[(len(A)//2)-1])/2

def mode_of_array(A):
    return int(stats.mode(A)[0])

T=int(input())
A=list(map(int,input().split()))
print(mean_of_array(A))
print(median_of_array(A))
print(mode_of_array(A))
