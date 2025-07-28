def selection_sort(my_list):
    # Outer loop: Iterate through the list to find the correct position for each element
    for i in range(len(my_list) - 1):
        min_index = i  # Assume the current index holds the smallest element

        # Inner loop: Find the index of the smallest element in the unsorted portion of the list
        for j in range(i + 1, len(my_list)):
            if (
                my_list[j] < my_list[min_index]
            ):  # Compare current element with the smallest found so far
                min_index = j  # Update min_index if a smaller element is found

        # Swap the smallest element with the element at the current position
        if min_index != i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]  # Swap

    # Return the sorted list
    return my_list


# Example list to sort
print(selection_sort([3, 25, 14, 89, 1]))
