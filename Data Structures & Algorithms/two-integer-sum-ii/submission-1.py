class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l<r:
            cur_num = numbers[l] + numbers[r]
            if cur_num < target:
                l += 1
            elif cur_num > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []