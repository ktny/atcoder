N = int(input())

nums = []
i = 1
while True:
    a = 6**i
    b = 9**i
    if a <= 100000:
        nums.append(6**i)
    else:
        break    
    if b <= 100000:
        nums.append(9**i)
    i += 1
nums.append(1)
nums.sort(reverse=True)
print(nums)

ans = 0
while True:
    print(N)
    if N == 0:
        print(ans)
        exit()
    for n in nums:
        if N >= n:
            N -= n
            ans += 1
            break