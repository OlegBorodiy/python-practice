def my_zip(first_object, second_object, index, my_dict):
    my_dict[first_object[-index]] = second_object[-index]
    if index == 1:
        my_dict[first_object[-1]] = second_object[-1]
        return my_dict
    else:
        return my_zip(first_object, second_object, index - 1, my_dict)


data_list = ['College', 'Wood', '981']
data_tuple = (1, 2, 3)
min_index = min(len(data_list), len(data_tuple))
clear_dict = dict()
new_zip = my_zip(data_list, data_tuple, min_index, clear_dict)

print(new_zip)