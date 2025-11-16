n = [5,3,2,2,1,5,5,7,5,10]
m = [10,1,9,5,4,2,4,9]

def hashing(n,m):
  for i in range(len(m)):
    count = 0
    for j in range(len(n)):
      if i == j:
        count += 1
  return count      
print(hashing(n,m))