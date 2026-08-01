class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        candidate=0

        for i in nums:
            if count==0:
                candidate=i
                count=1
            elif candidate==i:
                count+=1
            else:
                count-=1
        
        if nums.count(candidate)> n//2:
            return candidate
        
        return -1