class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        du = set()
        for i in nums:
            if i in du:
                return True
            du.add(i)
        return False