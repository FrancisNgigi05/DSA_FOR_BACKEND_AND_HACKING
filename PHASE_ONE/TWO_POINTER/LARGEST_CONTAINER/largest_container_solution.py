from typing import List
def max_water(heights:List[int], left_height: int, right_height: int) -> int:
    height = min(heights[left_height], heights[right_height])
    # Get the width
    width = right_height - left_height
    # Starting max water
    max_water = height * width
    # Checking which pointer to move forward according to height coz height is
    # the new factor determining new max_water
    if heights[left_height] < heights[right_height]:
        left_height += 1
    else:
        right_height -= 1

    return max_water, left_height, right_height

# Input: Array[] => Each element represents height
# Output: Int => Max_volume
def largest_container(heights: List[int]) -> int:
    # Checking if inputed data is valid
    if len(heights) == 0 or len(heights) < 1:
        return('Invalid')
    
    # left, right = 0, len(heights) - 1
    # # Get minimum height to prevent overflow

    # height = min(heights[left], heights[right])
    # # Get the width
    # width = right - left
    # # Starting max water
    # max_water = height * width
    # # Checking which pointer to move forward according to height coz height is
    # # the new factor determining new max_water
    # if heights[left] < heights[right]:
    #     left += 1
    # else:
    #     right -= 1
    max_water_vol, left, right= max_water(heights, 0, len(heights) - 1)
    
    while left < right:
        # height = min(heights[left], heights[right])
        # width = right - left
        # possible_new_max_water = height * width
        # if possible_new_max_water > max_water:
        #     max_water = possible_new_max_water
        # if heights[left] < heights[right]:
        #     left += 1
        # else:
        #     right -= 1
        possible_new_max_water_vol, left, right = max_water(heights, left, right)
        
        if possible_new_max_water_vol > max_water_vol:
            max_water_vol = possible_new_max_water_vol

    return max_water_vol
# Input data
heights = [2, 7, 8, 3, 7, 6]
# Expected output: 24
print(largest_container(heights=heights))