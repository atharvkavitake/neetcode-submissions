class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2

            count = 1
            load = 0

            for w in weights:
                if load + w > mid:
                    count += 1
                    load = w
                else:
                    load += w

            if count <= days:
                high = mid
            else:
                low = mid + 1

        return low