# https://cses.fi/problemset/task/2205

def solve(n):
    b = ['0', '1']
    k = 1
    while (k < n):
        # converting to gray
        # using mirror technique
        b += b[::-1]
        for i in range(2 ** (k + 1)):
            if i < (2 ** (k)):
                b[i] = '0' + b[i]
            else:
                b[i] = '1' + b[i]
        k += 1
    return b

def main():
    n = int(input())
    b = solve(n)

    # printing the gray code
    for i in b:
        print(i)

if __name__ == "__main__":
    main()
