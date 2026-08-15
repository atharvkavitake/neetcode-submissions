class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n=len(nums)
        first=-1
        last=-1

        start=0
        end=n-1
        
        while start<=end:
            mid=(start+end)//2

            if nums[mid]==target:
                first=mid
                end=mid-1

            elif target<nums[mid]:
                end=mid-1

            else:
                start=mid+1

        
        start=0
        end=n-1
        
        while start<=end:
            mid=(start+end)//2

            if nums[mid]==target:
                last=mid
                start=mid+1

            elif target<nums[mid]:
                end=mid-1

            else:
                start=mid+1

        return[first,last]