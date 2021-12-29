# https://cses.fi/problemset/task/1754

def solve(a, b):
    x = 2 * a - b
    y = 2 * b - a
    if x >= 0 and y >= 0 and x % 3 == 0 and y % 3 == 0:
        return "YES"
    return "NO"

def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        print(solve(a, b))

if __name__ == "__main__":
    main()
