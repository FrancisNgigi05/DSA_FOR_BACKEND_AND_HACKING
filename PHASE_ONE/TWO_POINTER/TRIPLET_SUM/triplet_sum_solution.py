from typing import List

# Function is checking if there are three numbers in the list 
# that can be added to get a sum of 3
# @parameter: List
# Return: List
def triplet_sum_brute_force(nums: List[int]) -> List[int]:
    n = len(nums)
    # To get unique values
    triplets = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(triplet)
    
    return[list(triplet) for triplet in triplets]


# a + b + c = 0
# b + c = -a
def pair_sum_sorted(nums:List[int], target: int) -> List[int]:
    # variable to store the pairs
    pairs = []
    # Initialize the pointers
    left, right = 0, len(nums) - 1
    # Edge case to avoid pointers from meeting
    while left < right:
        # store the total to compare with target
        total = nums[left] + nums[right]
        
        if total == target:
            pairs.append([nums[left], nums[right]])
            left += 1 # To avoid duplicate '[b, c]' values
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif total < target:
            left += 1
        else:
            right -= 1

    return pairs


def triplet_sum(nums:List[int]):
    # Sort the list
    nums.sort()
    # Variable to store the triplets
    triplets = []
    for i in range(len(nums)):
        target = nums[i]

        if target > 0:
            break
        # avoiding duplicate target values
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        pairs = pair_sum_sorted(nums[i + 1:], target=-target)
        for pair in pairs:
            triplets.append([target] + pair)
    
    return triplets


nums = [0, -1, 2, -3, 1]


brute_force_result = triplet_sum_brute_force(nums=nums)
result =triplet_sum(nums=nums)
# Explected Output: [[-3, 1, 2], [-1, 0, 1]]
print(brute_force_result)
print(result)