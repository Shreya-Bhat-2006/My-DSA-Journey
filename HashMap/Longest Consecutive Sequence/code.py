class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0

        s = set(nums)

        for i in s:
            # i is the beginning of a sequence
            if i - 1 not in s:
                count = 1

                # Count consecutive numbers
                while i + count in s:
                    count += 1

                ans = max(ans, count)

        return ans