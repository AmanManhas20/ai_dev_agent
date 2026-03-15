
def merge_sort(input_list: list) -> list:
    """
    Sorts a list using the merge sort algorithm.

    Args:
    input_list (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left_half = input_list[:mid]
    right_half = input_list[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left: list, right: list) -> list:
    """
    Merges two sorted lists into a single sorted list.

    Args:
    left (list): The first sorted list.
    right (list): The second sorted list.

    Returns:
    list: The merged sorted list.
    """
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


if __name__ == "__main__":
    example_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = merge_sort(example_list)
    print("Original list:", example_list)
    print("Sorted list:", sorted_list)
