s = input()
K = int(input())

N = len(s)
words = set()
for i in range(N):
    # 辞書順にK番目の文字列は長くてもK文字しかない
    for j in range(i+1, i+K+1):
        w = s[i:j]
        if w not in words:
            words.add(w)

print(sorted(list(words))[K-1])



