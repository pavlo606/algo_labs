def get_smallest_subarray_to_sort(array_input: list[int], reverse: bool = False) -> tuple[int, int]:
    first_index = -1
    last_index = -1
    array = array_input[::-1] if reverse else array_input

    for i in range(1, len(array)):
        key = array[i]

        if key >= array[i - 1]:
            continue

        last_index = i

        j = i - 1
        while j >= 0 and key < array[j]:
            if first_index == -1 or first_index > j:
                first_index = j

            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

    if not reverse or first_index == -1:
        return (first_index, last_index)
    else:
        return (len(array)-last_index-1, len(array)-first_index-1)