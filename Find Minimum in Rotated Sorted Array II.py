class Solution:
    def findMin(self, nums: List[int]) -> int:
        output: int = nums[0]
        left: int = 0
        right: int = len(nums) - 1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            output = min(output, nums[middle])
            if nums[middle] > nums[right]: left = middle + 1
            elif nums[middle] > nums[left]: right = middle - 1
            else:
                left += 1
                right -= 1
        return output
