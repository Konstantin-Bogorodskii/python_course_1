list_of_nums = [1, 3, 5, 7, 6, 8, 9, 20]

# Поменять элементы массива местами
list_of_nums[3], list_of_nums[2] = list_of_nums[2], list_of_nums[3]
print(list_of_nums)  # [1, 3, 7, 5]

# Получить произвольный интервал (список от и до)
print(list_of_nums[0:3])  # [1, 3, 7]
print(list_of_nums[0:len(list_of_nums)])  # [1, 3, 7, 5]

list_of_nums_interval = list_of_nums[0:2]  # [1, 3]
print(list_of_nums_interval)

# Получить полный список

print(list_of_nums[:len(list_of_nums)])  # [1, 3, 7, 5] первый индекс автоматически подставился
print(list_of_nums[:])  # [1, 3, 7, 5] первый в последний индекс автоматически подставились

# Получить слайс с каждым вторым элементом
# print(list_of_nums[0:len(list_of_nums):2])  # [1, 7, 6, 9]

slice_res_1 = list_of_nums[::2]
# slice_res_2 = list_of_nums[::2]
print(slice_res_1)
# print(slice_res_2)
