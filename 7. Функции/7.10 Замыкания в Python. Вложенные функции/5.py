def function(t='tuple'):
    def function_2(s):
        m = map(int, s.split())
        return list(m) if t == "list" else tuple(m)
    return function_2

t_p = input()
nums = input()

lst = function(t_p)(nums)

print(lst)
