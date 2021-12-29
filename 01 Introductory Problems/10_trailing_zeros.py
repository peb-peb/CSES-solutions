# https://cses.fi/problemset/task/1618

def solve(n):
    cnt = 0
    while n >= 5:
        cnt += n // 5
        n //= 5
    return cnt

def main():
    n = int(input())
    print(solve(n))

if __name__ == "__main__":
    main()
