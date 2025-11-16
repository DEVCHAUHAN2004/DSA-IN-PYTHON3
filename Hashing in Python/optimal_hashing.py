n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 1, 9, 5, 4, 2, 4, 9]

# Step 1: Create hash list for counting
hash_list = [0] * 11  # 0–10 (max value = 10)

# Step 2: Count frequencies of numbers in n
for num in n:
    hash_list[num] += 1

# Step 3: Print results in "num : count" format
for num in m:
    if num < 1 or num > 10:
        print(f"{num} : 0")
    else:
        print(f"{num} : {hash_list[num]}")


# 10 : 1
# 1 : 1
# 9 : 0
# 5 : 4
# 4 : 0
# 2 : 2
# 4 : 0
# 9 : 0