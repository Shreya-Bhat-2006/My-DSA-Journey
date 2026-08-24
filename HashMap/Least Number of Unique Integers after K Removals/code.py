class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}

        # Count frequency
        for i in arr:
            d[i] = d.get(i, 0) + 1

        # Create frequency buckets
        buckets = [[] for _ in range(len(arr) + 1)]

        for num, freq in d.items():
            buckets[freq].append(num)

        unique = len(d)

        # Process smallest frequencies first
        for freq in range(1, len(arr) + 1):

            for num in buckets[freq]:

                if freq <= k:
                    k -= freq
                    unique -= 1
                else:
                    return unique

        return unique