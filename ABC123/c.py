import math
N,*C = [int(input()) for i in range(6)]
print(math.ceil(N / min(C)) + 4)