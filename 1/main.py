def find_single_numbers(arr):
    xor = 0
    for num in arr:
        xor ^= num
    diff_bit = xor & -xor
    x, y = 0, 0
    for num in arr:
        if num & diff_bit:
            x ^= num
        else:
            y ^= num
    return sorted([x, y])

# Example usage:
arr1 = [1, 2, 3, 2, 1, 4]
arr2 = [2, 1, 3, 2]
print(find_single_numbers(arr1))  # Output: [3, 4]
print(find_single_numbers(arr2))  # Output: [1, 3]
