# Brute force solution
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i,x in enumerate(nums):
        for j,y in enumerate(nums[i+1:]):
            if x+y == target:
                return [i,j+i+1]


# Hash Table two pass
def twoSum(nums, target):
    map_ = {}
    for i, x in enumerate(nums):
        map_[x] = i
    for j, x in enumerate(nums):
        complement = target - x
        if complement in map_ and map_.get(complement) != j:
            return [j, map_.get(complement)]


# Hash Table one pass
def twoSum(nums, target):
    map_ = {}
    for i,x in enumerate(nums):
        complement = target - x
        if complement in map_:
            return [map_.get(complement), i]
        map_[x] = i
