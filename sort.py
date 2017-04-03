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
            temp_dict = {count}
            temp_dict.update(new_dict)
            main_dict.update(temp_dict)
            new_dict = {}
            count += 1
        else:
            d_k_v[1] = d_k_v[1].replace("\n", "")
            new_dict[d_k_v[0]] = d_k_v[1]


    print(main_dict)

    m_list = sorted(main_dict)
    f = open('rezult', 'w')
    for key in m_list:
        f.write(str(main_dict[key][1]) + "\n")


    # for key in sorted(main_dict):
    #     # sort_list.update((key, main_dict[key]))
    #     print(key, main_dict[key])




def sorting(a):
    b = {}
    for element in a:
        print(element.keys())
        b.update(element)
        print(sorted(b))

correct(dict_list, main_dict)


