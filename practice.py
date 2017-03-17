


# implement a function that will flatten two lists up to a maximum given depth:
# def flatten(list_a, list_b, max_depth)
list_a = [4, [2, 8], 4, 10, [22, 44, [55, 66]]]
list_b = [5, 6,[[[2], 3], 4], 7, 8]
list_c = [[1,2,3], [4,5,6], [7,8,9]]
max_depth = 0
the_list = list_a + list_b
print(type(list_a), type(list_b))

# def flatten(list_a, list_b, max_depth):
#


def my_way(my_list):
    for x in range(max_depth):
        for elem in my_list:
            print(elem)
            max_depth - 1
        try:
            pass
         except TabError:
             elem.append(my_list)




my_way(the_list)


def flatten_list(l, depth):

    assert depth >= 0
    if depth == 0:
        return l

    result = []
    for list_element in l:
        try:
            result.extend(
                flatten_list(iter(list_element), depth - 1)

            )
        except TypeError:
            result.append(list_element)
    return result


# flatten_list(list_a, max_depth)
# print(flatten_list(list_a, max_depth))
