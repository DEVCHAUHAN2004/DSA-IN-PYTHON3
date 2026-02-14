class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        d = {}
        count = 0

        for i in range(n):
            for j in range(n):
                s = nums1[i] + nums2[j]
                if s in d:
                    d[s] += 1
                else:
                    d[s] = 1

        for k in range(n):
            for l in range(n):
                target = -(nums3[k] + nums4[l])

                if target in d:
                    count += d[target]
        return count                            