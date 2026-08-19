class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        base = nums.count(k)
        answer = base

        for v in range(1, 51):
            if v == k:
                continue

            current = 0
            best = 0

            for num in nums:
                if num == v:
                    current += 1
                elif num == k:
                    current -= 1

                if current < 0:
                    current = 0

                best = max(best, current)

            answer = max(answer, base + best)

        return answer