class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Example: nums = [3,4,5,6], target = 7
        # Goal: find indices i < j where nums[i] + nums[j] = target.

        # Rearrange:
        # nums[j] = target - nums[i]

        # Store each previously seen number and its index.

        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            # Trace:
            # i=0, num=3, complement=4, seen={}
            # -> 4 not found; store:{3:0}

            # i=1, num=4, complement=3, seen={3:0}
            # -> 3 found at index 0; return [0, 1]

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i