class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # n = number of input elements.
        #
        # Invariant: "seen" contains all previously processed values.
        
        seen = set()

        for i in nums:
            # At most n iterations.
            # Hash set lookup: expected O(1).            
            if i in seen:
                return True

            # Hash set insertion: expected amortized O(1).            
            seen.add(i)

        return False

        # Time derivation:
        # n iterations * constant expected cost per iteration
        # = O(n) expected time.
        #
        # Space derivation:
        # At most one new value stored per iteration.
        # After n iterations, at most n values are stored.
        # = O(n) auxiliary space.