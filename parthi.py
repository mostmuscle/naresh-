num = int(input("Enter a number:"))
factional = 1
if num < 0:
  print("Factorial dose not exist for negative numbers")
elif num == 0:
  print("The Factorial 0 of is 1")
else:
  for i in range(1,num + 1):
    factorial=factorial*i
