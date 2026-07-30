class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        xorr=0
        for num in nums:
            xorr=xorr^num
        return xorr
        