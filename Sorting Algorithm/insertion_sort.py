def insertion_sort(my_list):
    # Outer loop: Iterate through the list starting from the second element
    for i in range(1, len(my_list)):
        temp = my_list[i]  # Store the current element to be inserted
        j = i - 1  # Start comparing with the previous element

        # Inner loop: Shift elements to the right to make space for the current element
        while j >= 0 and temp < my_list[j]:
            my_list[j + 1] = my_list[j]  # Shift the larger element one position to the right
            j -= 1  # Move to the previous element

        # Insert the current element into its correct position
        my_list[j + 1] = temp

    # Return the sorted list
    return my_list

# Example list to sort
print(insertion_sort([3, 25, 14, 89, 1]))