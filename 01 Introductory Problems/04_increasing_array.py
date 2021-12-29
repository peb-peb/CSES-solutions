# https://cses.fi/problemset/task/1094

""" TLE
def solve(n, x):
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] > x[j]:
                res += x[i] - x[j]
                x[j] = x[i]
    return res
"""

def solve(n, x):
    res = 0
    i = 0
    while i < n - 1:
        if x[i] > x[i + 1]:
            res += x[i] - x[i + 1]
            x[i + 1] = x[i]
        i += 1
    return res

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(solve(n, x))

if __name__ == "__main__":
    main()
