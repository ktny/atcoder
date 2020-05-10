s = input()
from collections import Counter
print(sorted(Counter(s).items(), key=lambda x: -x[1])[0][0])