class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = ""
        len_short = float('inf')
        short_str = ""
        for string in strs:
            if len(string) < len_short:
                len_short = len(string)
                short_str = string

        for i in range(len_short):
            for string in strs:
                if short_str[i] != string[i]:
                    return out
            out += short_str[i]
        
        return out
            
        

            