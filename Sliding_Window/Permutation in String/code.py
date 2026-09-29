class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        d1 = {}

        for i in s1:
            d1[i] = d1.get(i, 0) + 1

        d2 = {}
        k = len(s1)

        for r in range(len(s2)):

            d2[s2[r]] = d2.get(s2[r], 0) + 1

            if r >= k:
                lc = s2[r - k]

                d2[lc] -= 1

                if d2[lc] == 0:
                    del d2[lc]

            if d1 == d2:
                return True

        return False