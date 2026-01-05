# Function is to find the maximum sum of a contiguous subarray of size k
# Input: Array, k
# Output: max sum (int)
from typing import List
def max_subarray_sum(arr: List[int], k: int) -> int:
    # Length of array
    n = len(arr)
    left = 0
    # Get the first sum of window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for right in range(k, n):
        window_sum += arr[right]
        window_sum -= arr[left]
        left += 1

        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [5, 2, -1, 0, 3]

first_result = max_subarray_sum(arr=arr, k=3)
print(first_result) # Expeceted Output: 6

arr2 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
second_result = max_subarray_sum(arr=arr2, k=4)
print(second_result) # Expected Output: 39