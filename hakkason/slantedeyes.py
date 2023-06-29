s, n = map(int, input().split())


def f(s, n):
    return "OK" if s > n or s == n else "NG"


print(f(s, n))
