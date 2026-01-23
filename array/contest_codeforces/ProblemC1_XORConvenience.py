def generate(n):
    if n == 3:
        return [2,1,3]
    p = [0]*(n+1)
    p[n] = 1
    for i in range(2,n):
        p[i] = i ^ 1
    p[1] = n if n % 2 == 0 else n - 1
    return p[1:]

t = int(input())
for _ in range(t):
    n = int(input())
    print(*generate(n))
