def minMax(my_list):
   
    min_num = min(my_list)
    max_num = max(my_list)

    min_rank = my_list.index(min_num) + 1
    max_rank = my_list.index(max_num) + 1

    print(f"min: {min_num}, rank: {min_rank}")
    print(f"max: {max_num}, rank: {max_rank}")

my_list = [3, 1, 5, 4, 2]
minMax(my_list)
