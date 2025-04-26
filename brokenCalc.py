class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # T: O(log target), S: O(1)
        operations = 0
        while target > startValue:
            operations += 1
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
        return operations + (startValue - target)
