class Solution(object):
    def maxArea(self, height):
        if len(height) == 2:
            return min(height[0], height[1])
            
        i = 0
        j = len(height) - 1

        result = 0

        while i < j:
            if result < (j - i) * min(height[i], height[j]):
                result = (j - i) * min(height[i], height[j])

            if height[j] < height[i]:
                j = j - 1
            else:
                i = i + 1
            
        return result
        