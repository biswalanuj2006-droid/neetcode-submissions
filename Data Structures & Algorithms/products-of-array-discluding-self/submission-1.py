class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        rows = len(nums)
        res = [1] * rows

        prod = 1

        for i in range(rows):
            res[i] = prod
            prod *= nums[i]

        prod = 1

        for i in range(rows - 1, -1, -1):
            res[i] *= prod
            prod *= nums[i]

        return res