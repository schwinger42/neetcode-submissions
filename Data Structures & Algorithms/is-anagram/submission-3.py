class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # If the strings have different lengths,
        # they cannot contain identical character counts.
        if len(s) != len(t):
            return False
        
        # Dictionary:
        # key = character
        # value = number of occurences in "s"
        count = {}

        for char in s:
            # get(char, 0) returns the existing count,
            # or 0 if the character is not yet in count.
            count[char] = count.get(char, 0) +1
        
        # Process every character in "t".
        for char in t:
            # If "t" contains a character absent from "s",
            # or we've already exhausted all its occurrences,
            # then "t" cannot be an anagram of "s"
            if char not in count or count[char] == 0:
                return False

            # Otherwise, consume one occurrence.
            count[char] -= 1

        # Every character in t was matched successfully.
        # Because len(s) == len(t), all counts must now be 0.
        return True
        