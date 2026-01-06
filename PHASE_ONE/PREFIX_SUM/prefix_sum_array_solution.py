from typing import List
# Input: Arr[] => Original array
# Output: Arr[] => Array with prefix sum

def prefix_sum_array_solution(arr: List[int]) -> List[int]:
    # Check if the list is empty
    if not arr:
        return
    # Get length of original array
    n = len(arr)
    # Create a new duplicate array
    prefix_sum_arr = [0] * n
    # Inserting the first element of the original array to my new array
    prefix_sum_arr[0] = arr[0]
    # Iterating through the size of original array
    for i in range(1, n):
        # Finding the next prefix sum element
        prefix_sum_arr[i] = prefix_sum_arr[i - 1] + arr[i]
    return prefix_sum_arr

original_arr = [10, 20, 10, 5, 15]

print(prefix_sum_array_solution(arr=original_arr)) # Expected Output: [10, 30, 40, 45, 60]