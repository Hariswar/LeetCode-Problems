class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_length, max_lenthFound,start = 0,0,0
        N = len(s)
        i = 0
        lookup = {}
        while i<N:
            if s[i] not in lookup:
                current_length = current_length + 1
            else: 
                start = max(start,lookup[s[i]])
                current_length = i - start
            lookup[s[i]] = i
            max_lenthFound = max(current_length,max_lenthFound)
            i = i + 1
        return max_lenthFound