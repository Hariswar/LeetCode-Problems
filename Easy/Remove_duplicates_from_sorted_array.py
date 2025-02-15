class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first_elementOfnum = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[first_elementOfnum] = nums[i]
                first_elementOfnum += 1
        return first_elementOfnum