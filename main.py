print("Welcome to Python Pizza Delivery")
bill = 0
size = input("What size of pizza do you want ? S, M or L :")
if size == "S":
  bill += 15
  print("Small size pizza cost $15.")
elif size == "M" :
  bill += 20
  print("Medium size pizza cost $20.")
else:
  bill += 25
  print("Large size pizza is $25.")
add_peperoni = input("Do you want peperoni ? Y or N:")
if add_peperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
extra_cheese = input("Do you want extra cheese ? Y or N :")
if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is ${bill}")

  