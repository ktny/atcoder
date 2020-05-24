s = input()

g = 0
p = 0
win = 0
lose = 0

for hand in s:
    if p == g:
        g += 1
        if hand == 'p':
            lose += 1
    else:
        p += 1
        if hand == 'g':
            win += 1

print(win-lose)