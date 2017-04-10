# Given a file containing a list of dictionaries implement a sorting algorithm (of your choosing) that will sort the list
# based on the dictionary keys.
# The dictionary keys will contain alphabetic characters while the values will be integers.
# The rule for comparing dictionaries between them is:
# if the value of the dictionary with the lowest alphabetic key is lower than the value of the other dictionary with the
# lowest alphabetic key, then the first dictionary is smaller than the second.
# if the two values specified in the previous rule are equal reapply the algorithm ignoring the current key.
#
# The input is a file containing the list of dictionaries. Each dictionary key value is specified on the same line in the
# form <key> <whitespace> <value>. Each list item is split by an empty row. The output is a file containing a list of
# integers specifying the dictionary list in sorted order. Each integer identifies a dictionary in the order they were
# received in the input file.


dict_list = open("file.py", "r").readlines()

main_dict = {}


def correct(dict_list, main_dict):
    count = 1
    new_dict = {}
    for line in dict_list:
        d_k_v = line.split(" ")
        if d_k_v[0] == '\n':
            temp_dict = {}
            count = str(count)
            temp_dict[count] = new_dict
            main_dict.update(temp_dict)
            new_dict = {}
            count = int(count)
            count += 1
        else:
            d_k_v[1] = d_k_v[1].replace("\n", "")
            new_dict[d_k_v[0]] = d_k_v[1]

    print(main_dict)


def master_orders_list(main_dict):
    list_tulp = []
    for dict in main_dict:
        if len(main_dict[dict]) > 1:
            temp = []
            for sub_dict in main_dict[dict]:
                temp.append(sub_dict)
                temp.sort()
                t2 = dict, temp[0]
            list_tulp.append(t2)
        else:
            for sub_dict in main_dict[dict]:
                t1 = dict, sub_dict
                list_tulp.append(t1)
    print(list_tulp)
    return list_tulp



def bubble_sort(items):

    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j][1] > items[j+1][1]:
                items[j], items[j + 1] = items[j + 1], items[j]  # Swap!
    print(items)
    f = open('rezult', 'w')
    for key in items:
        f.write(key[0] + "\n")

correct(dict_list, main_dict)
items = master_orders_list(main_dict)
bubble_sort(items)

