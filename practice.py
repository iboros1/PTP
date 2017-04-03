# implement a function that will flatten two lists up to a maximum given depth:
# def flatten(list_a, list_b, max_depth)


list_a = [4, [2, 8], 4, 10, [22, 44, [55, 66]]]
list_b = [5, 6, [[[2], 3], 4], 7, 8]
# max_depth = int(raw_input("Max: "))

max_depth = 3

def flat(list_a):
    count=0
    for item in list_a:
        if isinstance(item, list):
            count += flat(item)
    return count+1



def flatten_list(l_a, l_b, depth):
    a = flat(list_a)
    b = flat(list_b)
    if a or b < max_depth:
        print("Update max_depth")
    else:
        print(fl_list(l_a, depth))
        print(fl_list(l_b, depth))

def fl_list(l, depth):
    assert depth >= 0
    if depth == 0:
        return l

    result = []
    for list_element in l:
        try:
            result.extend(
                fl_list(iter(list_element), depth - 1)

            )
        except TypeError:
            result.append(list_element)
    return result


# flatten_list(list_a, max_depth)
flatten_list(list_a, list_b, max_depth)



def sortListFromFile(fileName, outputFileName):

    sortListFromFile('nonexistentfile','output.txt')

    l = []
    with open(fileName, 'r') as f:
        elem = {}
        for line in f:
            if line.strip():
                line = line.split()
                elem[line[0]] = line[1]
            else:
                l.append(elem)
                elem = {}
        l.append(elem)
    f.closed
    with open(outputFileName, 'w+') as f:
        for list_elem in quicksort(l):
            f.write(str(l.index(list_elem)) + '\n')
f.closed
