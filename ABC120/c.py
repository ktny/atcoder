S = input()
t = []
for s in S:
    if len(t) == 0:
        t += s
    elif t[-1] != s:
        t.pop()
    else:
        t += s
print(len(S)-len(t))