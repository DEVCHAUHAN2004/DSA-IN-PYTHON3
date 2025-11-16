s = "azyxyyzaazxyazyaaazxyy"
q = ["a", "x", "z", "y", "d"]

# Step 1: Count character frequencies using dictionary
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

# Step 2: Print frequency for each query character
for ch in q:
    if ch in freq:
        print(f"{ch} : {freq[ch]}")
    else:
        print(f"{ch} : 0")
