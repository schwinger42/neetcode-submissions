class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Let n = len(nums), the number of input elements.
        #
        # Approach:
        # Store previously encountered values in a hash set.
        # For each value, check whether it has appreaed boere.
        
        seen = set()

        # TIME COMPLEXITY:
        # 1. The loop runs at most n times.
        # 2. "i in seen" takes O(1) expected time per lookup.
        # 3. "seen.add(i)" takes O(1) amortized expected time.
        #
        # Therefore, for n iterations:
        # Expected total work grows as n * constant = O*(n)

        for i in nums:
            if i in seen:
                return True
            
            seen.add(i)

        return False