def count_in_list(lst, value):
    """ Count how many times 'value' appear in 'list' """

    count = 0
    for x in lst:
        if x == value:
            count += 1
    return count
