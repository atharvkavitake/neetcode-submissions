class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
            
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                
                # Check left side
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                
                # Check right side
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                # If both sides are empty, plant a flower
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
                    
                    if n == 0:
                        return True
        
        return False