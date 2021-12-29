# https://cses.fi/problemset/task/1617

MOD = 1_000_000_007

def solve(n):
    res = 1
    for i in range(n):
        res *= 2
        res %= MOD
    return res

def main():
    n = int(input())
    print(solve(n))

if __name__ == "__main__":
    main()
