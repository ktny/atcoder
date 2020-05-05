N = int(input())
A = [int(input()) for i in range(N)]

for i in range(N-1):
    if A[i+1] == A[i]:
        print('stay')
    elif A[i+1] > A[i]:
        print('up', A[i+1]-A[i])
    else:
        print('down', A[i]-A[i+1])
