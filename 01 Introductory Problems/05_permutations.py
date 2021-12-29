# https://cses.fi/problemset/task/1070

def solve(n):
   # generating 5,3,1,...
    res = [i for i in range(n, 0, -1) if i % 2 != 0]
    # generating 6,4,2,...
    res += [i for i in range(n, 0, -1) if i % 2 == 0]
    return res

def main():
    n = int(input())
    if n == 2 or n == 3:
        print("NO SOLUTION")
    else:
        print(*solve(n))

if __name__ == "__main__":
    main()
