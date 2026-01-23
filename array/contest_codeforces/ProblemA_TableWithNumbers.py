t = int(input())
for _ in range(t):
    n, h, l = map(int, input().split())
    a = list(map(int, input().split()))
    valid_rows = sum(1 for x in a if x <= h)
    valid_cols = sum(1 for x in a if x <= l)
    max_pairs = min(valid_rows, valid_cols)
    print(max_pairs)
