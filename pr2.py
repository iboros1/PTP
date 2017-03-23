# P2. Merge 2 objects with any depth (including contained dictionaries, lists, sets, strings, integers, floats).
# Type mismatches should yield a tuple with the two elements. Examples:
# a = {'x': [1,2,3], 'y': 1, 'z': set([1,2,3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
# b = {'x': [4,5,6], 'y': 4, 'z': set([4,2,3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}
# Expected result:
# {'x': [1,2,3,4,5,6], 'y': 5, 'z': set([1,2,3,4]), 'w': 'qweqweasdf', 't': {'a': [1, 2, 3, 2]}, 'm': ([1], "wer")}


a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
b = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}


def anyw(a, b):
    for elem in a:
        if type(a[elem]) == list:
            listb(b, a, elem)
        if type(a[elem]) == int:
            intb(b, a, elem)
        if type(a[elem]) == str:
            strb(b, a, elem)
        if type(a[elem]) == set:
            setb(b, a, elem)
        if type(a[elem]) == dict:
            dictb(b, a, elem)

    return elem


def listb(b, a, elem):
    for item in b:
        if elem == item:
            if type(a[elem]) == type(b[item]):
                a[elem].extend(b[item])
            else:
                a[elem]= a[elem],  (b[item])
            print(a)


def intb(b, a, elem):
    for item in b:
        if elem == item:
            if type(a[elem]) == type(b[item]):
                a[elem] = b[item] + a[elem]
            print(a)


def strb(b, a, elem):
    for item in b:
        if elem == item:
            if type(a[elem]) == type(b[item]):
                a[elem] = str(b[item]) + str(a[elem])
            print(a)


def setb(b, a, elem):
    for item in b:
        if elem == item:
            if type(a[elem]) == type(b[item]):
                a[elem] = a[elem].union(b[item])
            # WIP add proper formating
            print(a)


def dictb(b, a, elem):
    for item in b:
        if elem == item:
            if type(a[elem]) == type(b[item]):
                a[elem]["a"] = a[elem]["a"] +b[item]["a"]

            print(a)

anyw(a, b)
