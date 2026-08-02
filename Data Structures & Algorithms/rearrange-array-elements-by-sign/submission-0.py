class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        pos=0
        neg=1

        for x in nums:
            if x>0:
                ans[pos]=x
                pos+=2

            else:
                ans[neg]=x
                neg+=2

        return ans        