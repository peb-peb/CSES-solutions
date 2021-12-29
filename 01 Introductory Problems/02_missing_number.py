# https://cses.fi/problemset/task/1083

def solve(n, A):
    B = set(i + 1 for i in range(n))
    return next(iter(B - A))

def main():
    n = int(input())
    a = set(map(int, input().split()))
    print(solve(n, a))

if __name__ == "__main__":
    main()
