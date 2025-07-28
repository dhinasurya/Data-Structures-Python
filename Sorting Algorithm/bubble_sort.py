def bubble_sort(my_list):
    # Outer loop: Controls the number of passes
    # Each pass ensures the largest unsorted element "bubbles up" to its correct position
    for i in range(
        len(my_list) - 1, 0, -1
    ):  # Start from the end and reduce the range with each pass
        # Inner loop: Compares adjacent elements
        for j in range(i):  # Iterate through the unsorted portion of the list
            # Compare the current element with the next element
            if (
                my_list[j] > my_list[j + 1]
            ):  # If the current element is greater, swap them
                # Swap the elements to move the larger one to the right
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    # Return the sorted list after all passes
    return my_list


# Example list to sort
my_list = [2, 5, 6, 1, 3]

# Print the sorted list
print(bubble_sort(my_list=my_list))
