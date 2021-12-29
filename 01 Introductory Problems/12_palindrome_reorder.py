# https://cses.fi/problemset/task/1755

from collections import Counter

def solve(s):
    cnt = Counter(s)
    odd_cnt = 0
    for value in dict(cnt).values():
        if value % 2 != 0:
            odd_cnt += 1
    if odd_cnt > 1:
        return "NO SOLUTION"

    pal = ''
    odd_key = ''
    for key, value in dict(cnt).items():
        if value % 2 == 0:
            pal += key * (value // 2)
        else:
            odd_key = key
    rev = pal[::-1]
    if odd_key != '':
        pal += odd_key * dict(cnt)[odd_key]
    pal += rev
    return pal

def main():
    s = input()
    print(solve(s))

if __name__ == "__main__":
    main()
