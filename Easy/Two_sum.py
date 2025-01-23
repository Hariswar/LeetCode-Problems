class Solution(object):
  def twoSum(self, nums, target): 
    for k in range(len(nums)):
      for i in range(k+1, len(nums)):
        if nums[k] + nums[i] == target:
             return [k, i]
    return []