# https://cses.fi/problemset/task/2165

def solve(res, n, s, t, d):
    if n == 1:
        res.append((s, d))
    else:
        solve(res, n - 1, s, d, t)
        res.append((s, d))
        solve(res, n - 1, t, s, d)

def main():
    n = int(input())
    res = []
    solve(res, n, 1, 2, 3)
    print(len(res))
    for a, b in res:
        print(a, b)

if __name__ == "__main__":
    main()
