n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 1, 9, 5, 4, 2, 4, 9]

freq_map = {}

# Step 1: Count frequency of elements in n
for num in n:
    if num in freq_map:
        freq_map[num] += 1
    else:
        freq_map[num] = 1

# Step 2: Print frequency for elements in m
for num in m:
    if num in freq_map:
        print(f"{num} : {freq_map[num]}")
    else:
        print(f"{num} : 0")

# 10 : 1
# 1 : 1
# 9 : 0
# 5 : 4
# 4 : 0
# 2 : 2
# 4 : 0
# 9 : 0