nums1 = list(map(int, input().split()))
m = int(input())

nums2 = list(map(int, input().split()))
n = int(input())

i = 0
j = 0
res = []

while i < m and j < n:
    if nums1[i] <= nums2[j]:
        res.append(nums1[i])
        i += 1
    else:
        res.append(nums2[j])
        j += 1

while i < m:
    res.append(nums1[i])
    i += 1

while j < n:
    res.append(nums2[j])
    j += 1

for k in range(len(res)):
    nums1[k] = res[k]

print(nums1)