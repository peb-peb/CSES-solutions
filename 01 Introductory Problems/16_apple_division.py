# https://cses.fi/problemset/task/1623

import math

# we use subsequences for all possible sequences
# we could generate this using binary numbers
def solve(n, p):
    total = sum(p)
    res = math.inf
    for i in range(1 << n):
        sub = []
        for j in range(n):
            if (i & (1 << j)):
                sub.append(p[j])
        res = min(res, abs(total - sum(sub) - sum(sub)))
    return res

def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(solve(n, p))

if __name__ == "__main__":
    main()
