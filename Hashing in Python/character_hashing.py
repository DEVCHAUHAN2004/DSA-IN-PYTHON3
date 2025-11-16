s = "azyxyyzaazxyazyaaazxyy"
q = ["a", "x", "z", "y", "d"]

# Step 1: Create a frequency array of size 26 for 'a' to 'z'
hash_list = [0] * 26

# Step 2: Count frequencies of each character in s
for ch in s:
    index = ord(ch) - ord('a')
    hash_list[index] += 1

# Step 3: Print frequency for each query character
for ch in q:
    index = ord(ch) - ord('a')
    print(f"{ch} : {hash_list[index]}")


# a : 7
# x : 4
# z : 4
# y : 6
# d : 0
