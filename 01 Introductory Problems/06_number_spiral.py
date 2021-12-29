# https://cses.fi/problemset/task/1071

def solve(y, x):
    n = max(y, x)
    r = n * (n - 1) + 1 # 1,3,7,13,21,...
    m = abs(y - x)
    if n % 2 == 0:
        if y < x:
            r -= m
        else:
            r += m
    else:
        if y > x:
            r -= m
        else:
            r += m
    return r

def main():
    for _ in range(int(input())):
        y, x = map(int, input().split())
        print(solve(y, x))

if __name__ == "__main__":
    main()
