# Дан список чисел nums и число target.
# Нужно найти такие два индекса в списке, чтобы сумма чисел по этим индексам
# была равна target.


nums = [2, 7, 11, 15]
target = 9
for index in range(len(nums)):
    for index_2 in range(index + 1, len(nums)):
        if nums[index] + nums[index_2] == target:
            print(nums[index], nums[index_2])

