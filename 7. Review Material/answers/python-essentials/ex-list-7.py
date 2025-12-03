max_number = max(num_of_each_item)
index_pos = num_of_each_item.index(max_number)
item = shopping_list[index_pos]
print(f"I will buy {max_number} {item}")