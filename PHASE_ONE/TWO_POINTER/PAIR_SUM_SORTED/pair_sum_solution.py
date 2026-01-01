from typing import List

# The function is supposed to check if there are two elements that can be added and have a sum == target
# Time complexity O(n ^ 2)
def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Getting the length of the array
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# The function below is two effieciently solve the above pair sum sorted problem using time complexity of O(n)
def two_pointer_pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Initializing pointers at both ends
    left, right = 0, len(nums) - 1

    # Edge case to avoid the pointers crossing or meeting at a point
    while left < right:
        total = nums[left] + nums[right]
        if total < target:
            left += 1
        elif total  > target:
            right -= 1
        else:
            return [left, right]
    return []



nums = [-5, -2, 3, 4, 6]
target = 7

result = []

result = pair_sum_sorted(nums=nums, target=target)
two_pointer_result = []

two_pointer_result = two_pointer_pair_sum_sorted(nums=nums, target=target)

# Expected result [2, 3]
print(result)
print(two_pointer_result)