# https://cses.fi/problemset/task/1069

def solve(n):
    cnt, k = [0], 0
    prv = n[0]
    for i in n:
        if i == prv:
            cnt[k] += 1
        else:
            prv = i
            cnt.append(1)
            k += 1
    return max(cnt)

def main():
    n = input()
    print(solve(n))

if __name__ == "__main__":
    main()
