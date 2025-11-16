count = 0
def greet():
  global count
  if count == 5:
    return 
  print("devil")
  count += 1 
  greet()

greet()
# devil
# devil
# devil
# devil
# devil