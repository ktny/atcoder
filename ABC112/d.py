s = 'jyvzzpunaolybipjvunfzpthre'


for i in range(26):
    tmp = ''
    for j in range(len(s)):
        c = chr(ord('a') + (ord(s[j]) - ord('a') + i) % 26)
        tmp += c
    print(i, tmp)