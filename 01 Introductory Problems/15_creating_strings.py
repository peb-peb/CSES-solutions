# https://cses.fi/problemset/task/1622

from itertools import permutations

""" TLE
# permuting using rotate method
def solve(perms, o, s):
    if s == "":
        if o not in perms:
            perms.append(o)
    else:
        for i in range(len(s)):
            solve(perms, o + s[0], s[1:])
            s = s[1:] + s[0]
"""

# using in-built function
def solve(perms, s):
    perms += [''.join(p) for p in permutations(s)]

def main():
    s = input()
    perms = []
    # solve(perms, "", ''.join(sorted(s))) # using rotate
    solve(perms, ''.join(sorted(s))) # using in-built function
    perms = set(perms)

    print(len(perms))
    for perm in perms:
        print(perm)

if __name__ == "__main__":
    main()
