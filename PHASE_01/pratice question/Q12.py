print("====recursion=====")
def countdown(n):
  if n==0:
    print("finished")
    return
  print(n)
  countdown(n-1)
countdown(5)