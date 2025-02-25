class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        for i in range(0, len(height)):
            if not prefix or height[i] >= height[prefix[-1]]:
                if not prefix:
                    prefix.append(i)
                elif prefix[-1] < suffix[-1]:
                    prefix.append(i)
                else:
                    break
            if not suffix or height[len(height) - 1 - i] >= height[suffix[-1]]:
                if not suffix:
                    suffix.append(len(height) - 1 - i)
                elif prefix[-1] < suffix[-1]:
                    suffix.append(len(height) - 1 - i)
                else:
                    break

        area = 0
        for i in range(0, len(prefix) - 1):
            for ix in range(prefix[i] + 1, prefix[i + 1]):
                area += height[prefix[i]] - height[ix]

        for i in range(0, len(suffix) - 1):
            for ix in range(suffix[i] - 1, suffix[i + 1], -1):
                area += height[suffix[i]] - height[ix]

        return area