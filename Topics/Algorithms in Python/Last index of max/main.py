def last_indexof_max(numbers):
    # write the modified algorithm here
    index = 0
    for x in range(1, len(numbers)):
        if numbers[x] >= numbers[index]:
            index = x
    return index
