class Solution:
    def romanToInt(self, s: str) -> int:
        s = s.lower()
        nums = {
            "i": 1,
            "v": 5,
            "x": 10,
            "l": 50,
            "c": 100,
            "d": 500,
            "m": 1000
        }
        nums_i = ["i", "v", "x", "l", "c", "d", "m"]
        subpairs = []

        for _ in enumerate(list(s)):
            try:
                print(list(s)[_[0]], nums[_[1]])
                if nums[_[1]] < nums[list(s)[_[0] + 1]]:
                    subpairs.append([_[0], _[0] + 1])
            except IndexError:
                continue
        
        ans = 0
        #debug: print(subpairs)
        sublist = set()
        for _ in subpairs:
            sublist.add(_[0])
            sublist.add(_[1])

        for _ in enumerate(list(s)):
            if _[0] in sublist:
                continue
            ans += nums[_[1]]
        
        for _ in subpairs:
            ans += nums[list(s)[_[1]]] - nums[list(s)[_[0]]]

        return ans