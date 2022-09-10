# jul 5 2022
from operator import le


def ConsecutiveSequence(nums):
    # nums = list(set(nums))
    # nums.sort()
    # count = 0
    # for i in range(len(nums)-1):
    #     if nums[i] + 1 == nums[i+1]:
    #         count += 1
    #     else:
    #         return nums[i]
    # return count + 1  
    num_set = set(nums)
        
    longest_sequence = 0
    for num in nums:
        if num - 1 in num_set:
            continue
        current_length = 1
        while num + 1 in num_set:
            num += 1
            current_length += 1
        longest_sequence = max(longest_sequence, current_length)
    return longest_sequence 

# nums = [0,3,7,2,5,8,4,6,0,1]
nums = [100,4,200,1,3,2]
# nums = [0,-1]
# nums = [9,1,4,7,3,-1,0,5,8,-1,6]
print("Longest Consecutive Sequence is", ConsecutiveSequence(nums))

