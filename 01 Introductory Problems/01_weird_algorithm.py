# https://cses.fi/problemset/task/1068

def solve(n):
    res = [n]
    while n > 1:
        if (n % 2 == 0):
            n //= 2
            res.append(n)
        else:
            n = n * 3 + 1
            res.append(n)
    return res

def main():
    n = int(input())
    print(*solve(n))

if __name__ == "__main__":
    main()
