class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(len(prefix)):
            for word in strs:
                if i >= len(word) or word[i] != prefix[i]:
                    return prefix[:i]

        return prefix
