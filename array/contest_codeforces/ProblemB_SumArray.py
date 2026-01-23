t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max_gap = 0
    for i in range(1, n):
        max_gap = max(max_gap, a[i] - a[i-1])
    print(max_gap)
