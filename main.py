def consecutive_fours(arr):
    current = arr [0]
    count = 1
    for item in arr[1:]:
        if current == item:
            count += 1
        else: # item = 2, current = 3
            current = item
            count = 1
        if count >= 4:
            return True
    return False

def sum_by_parity(arr):
    sum_even, sum_odd = 0, 0
    # arr [19, 201
    # index, item: 0 19
    # index,
    for index, item in enumerate(arr):
        if index % 2 == 0:
            sum_even += item
        else:
            sum_odd += item
    return [sum_even, sum_odd]

def expand_by_index (arr):
    res = []
    for index, item in enumerate(arr):
        for i in range (item):
            res.append (index)
    return res


def numerical_count(string):
    count = 0
    for item in string:
        if item.isdigit(): # string built-in functio
            count += 1
    return count


