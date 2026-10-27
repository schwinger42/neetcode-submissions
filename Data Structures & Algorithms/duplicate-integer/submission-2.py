class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Let n be the number of elements in numbs.
        #
        # TIME COMPLEXITY
        # 1. The loop executes at most n times.
        # 2. each set lookup taskes O(1) expected time.
        # 3. Each set insertion takes O(1) amortized expeected time.
        # 4. Without duplicates, there are n lookups and n insertions.
        # 5. Therefore, the total expected cost grows linearly with n: O(n)
        # SPACE COMPLEXITY
        #
        seen = set()                
        for i in nums:              
            if i in seen:           
                return True
            seen.add(i)
        return False