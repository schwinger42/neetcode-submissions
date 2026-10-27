
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # Problem: Return True if any value appears twice.
        # Example: [1, 2, 3, 3] -> True

        # Approach:
        # Track previously encountered values in a hash set.
        seen = set()

        for num in nums:
            # Trace (state BEFORE checking num):
            # num=1, seen={}       -> not found, add 1
            # num=2, seen={1}      -> not found, add 2
            # num=3, seen={1,2}    -> not found, add 3
            # num=3, seen={1,2,3}  -> found, return True

            if num in seen:
                return True

            seen.add(num)

        # Complexity derivation:
        # Let n = len(nums).
        #
        # TIME:
        # 1. The loop executes at most n times.
        # 2. Hash-set lookup has O(1) expected cost.
        # 3. Hash-set insertion has O(1) amortized expected cost.
        # 4. Each iteration therefore has constant expected cost.
        # 5. Total expected cost grows linearly with n.
        # => Expected time: O(n).
        #
        # SPACE:
        # 1. The set initially contains zero elements.
        # 2. Each iteration adds at most one distinct element.
        # 3. After at most n iterations, it stores at most n.
        # => Auxiliary space: O(n).

        return False
