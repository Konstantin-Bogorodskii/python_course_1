list_of_nums = [1, 2, 3, 4, 5]

# for num in list_of_nums:
#     print(num)

# for num in list_of_nums:
#     if num % 2 == 0:
#         print(num)
#     continue
#
# for num in list_of_nums:
#     if num == 3:
#         break
#     print(num)


my_range = range(1, 10)
print(my_range)  # range(1, 10)
print(range)  # <class 'range'>

my_range_list = list(my_range)
print(my_range_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_nums_range = range(2, 10, 2)
even_nums_range_list = list(even_nums_range)
print(even_nums_range_list)  # [2, 4, 6, 8]

list_of_nums_2 = [10, 11, 12, 13, 14, 15]

for i in range(len(list_of_nums_2)):
    print(i)  # index of each item
    list_of_nums_2[i] += 1

print(list_of_nums_2)  # [11, 12, 13, 14, 15, 16]
