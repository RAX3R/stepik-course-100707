def function(lst):
    v_min = min(lst)
    v_max = max(lst)
    v_sum = sum(lst)
    return f"Min = {v_min}, max = {v_max}, sum = {v_sum}"

print(function(list(map(int, input().split()))))
