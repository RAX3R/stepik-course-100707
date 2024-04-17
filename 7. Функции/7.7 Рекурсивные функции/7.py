nums = list(map(int, input().split()))

def two_l(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def sort_lst(s):
    if len(s) == 1:
        return s
    mid = len(s) // 2
    left = sort_lst(s[:mid])
    right = sort_lst(s[mid:])
    return two_l(left, right)

print(*sort_lst(nums))
