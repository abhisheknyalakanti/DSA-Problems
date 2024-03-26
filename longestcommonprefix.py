class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)<2:
            return strs[0]
        strs.sort()
        common_prefix=""
        index=0
        while index<len(strs[0]) and index<len(strs[-1]):
            if strs[0][index]==strs[-1][index]:
                common_prefix+=strs[0][index]
                index+=1
            else:
                break
        return common_prefix                
        