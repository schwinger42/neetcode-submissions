
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # PROBLEM:
        # Return True if any integer appears more than once.
        #
        # Example: [1, 2, 3, 3] -> True
        #          [1, 2, 3, 4] -> False
        #
        # APPROACH:
        # Store previously encountered integers in a hash set.
        # Check each integer BEFORE adding it to the set.

        seen = set()

        for i in nums:
            # TRACE for nums = [1, 2, 3, 3]:
            #
            # i=1, seen={}       -> not found -> add 1
            # i=2, seen={1}      -> not found -> add 2
            # i=3, seen={1,2}    -> not found -> add 3
            # i=3, seen={1,2,3}  -> found     -> return True

            if i in seen:
                return True

            seen.add(i)

        # We checked every element without finding a duplicate.
        return False

    # ANALYSIS (of hasDuplicate):
    #
    # Let n = len(nums).
    #
    # CORRECTNESS:
    # Before checking each number, seen contains all previously
    # encountered distinct numbers.
    # Therefore, if the current number is in seen,
    # that number must have appeared earlier.
    # If no such number is found, all values are unique.
    #
    # TIME COMPLEXITY:
    #
    # Step 1: Count iterations.
    # The loop processes at most n elements.
    #
    # Step 2: Determine the cost of each iteration.
    # Python sets use hash tables.
    # Under standard hashing assumptions:
    #   membership lookup -> expected constant time
    #   insertion         -> expected amortized constant time
    #
    # Step 3: Build a cost model.
    # Let a = expected cost of checking membership.
    # Let b = amortized expected cost of insertion.
    # Let c = other fixed work per iteration.
    # Let d = initialization and return overhead.
    #
    # For n distinct elements, no early return occurs.
    #
    # Expected work:
    # W(n) = d + (a+b+c) + ... + (a+b+c)  [n terms]
    #      = d + n(a+b+c)
    #
    # Since a, b, c, d do not grow with n,
    # expected work grows linearly with n.
    #
    # Expected time complexity: O(n).
    #
    # SPACE COMPLEXITY:
    #
    # Step 1: Identify additional storage.
    # The input nums already exists.
    # We create an additional hash set called seen.
    #
    # Step 2: Count how many elements it can store.
    # Each iteration inserts at most one new integer.
    # With n distinct integers, seen stores n elements.
    #
    # Step 3: Relate memory usage to n.
    # Assuming bounded storage per integer and hash-table
    # entry, additional memory grows linearly with n.
    #
    # Auxiliary space complexity: O(n).
