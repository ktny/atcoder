s,t = input().split()
if s[0] == 'B':
    s = 1 - int(s[1])
else:
    s = int(s[0])
if t[0] == 'B':
    t = 1 - int(t[1])
else:
    t = int(t[0])
print(abs(t-s))