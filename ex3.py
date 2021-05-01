# ex3

nums = [3, 5, 3, 1, 1]

result = 0
dict_res = {}
for i in nums:
    if i in dict_res:
        dict_res[i] += 1
    else:
        dict_res[i] = 1
for q in dict_res:
    if dict_res[q] == 1:
        result = q


print(result)
