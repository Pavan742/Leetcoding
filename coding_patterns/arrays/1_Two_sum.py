def twoSum(nums, target): 
    seen = {} # Store -> number : index
    for i in range(len(nums)):
        reminder = target - nums[i]
        if reminder in seen:
            return seen[reminder], i 
        seen[nums[i]] = i 
    return -1, -1 

print(twoSum([2,7,9,12,25,46,678,235], 19))

# Create a dictionary/hashmap to store each element's index
# For each element, calculate remainder = target - element
# Check if remainder exists in the hashmap
#   If yes, return (index of remainder, current index)
#   If no, add current element and its index to the hashmap
# If no pair sums to target, return (-1, -1)
