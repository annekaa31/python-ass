# ex1

nums = [2, 5, 1, 3, 4, 7]
#output [2,3,5,4,1,7]

arr_x = []
arr_y = []
result = []
med = len(nums)/2

for index in range(0, len(nums)):
    if index < med:
        arr_x.append(nums[index])
    else:
        arr_y.append(nums[index])

for j in range(0, len(arr_x)):
    result.append(arr_x[j])
    result.append(arr_y[j])
print(result)
