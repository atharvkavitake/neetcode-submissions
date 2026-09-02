class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)

        while low<high:
            mid=(low+high)//2

            count=1
            total=0
            
            for num in nums:
                if total+num>mid:
                    count+=1
                    total=num
                else:
                    total+=num

            if count>k:
                low=mid+1
            else:
                high=mid

        return low