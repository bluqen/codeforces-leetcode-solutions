class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefs = []
        if strs[0] == "":
            return ""
        for __ in range(max([len(x) for x in list(strs)])):
            common = ""
            end = False
            try:
                for _ in strs:
                    if _[__] != common and common != "":
                        common = ""
                        end = True
                        break
                    else:
                        common = _[__]
            except IndexError:
                break
            prefs.append(common)
            if end:
                break
        
        return "".join(prefs)

print(Solution().longestCommonPrefix(["ab", "abc"]))