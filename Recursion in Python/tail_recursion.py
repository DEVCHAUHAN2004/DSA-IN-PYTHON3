count = 0
def greet():
  global count
  if count == 5:
    return 
  count += 1
  greet()
  print("dev")

greet()  

# dev
# dev
# dev
# dev
# dev