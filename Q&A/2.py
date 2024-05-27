
def unique_list(num_list):
  unique_num_list = []
  for num in num_list:
    if num not in unique_num_list:
      unique_num_list.append(num)
  return unique_num_list


num_list = [1, 2, 3, 4, 5, 5, 6, 7, 7, 7, 8, 8, 9]
unique_nums = unique_list(num_list)
print(unique_nums)