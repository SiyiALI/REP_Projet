import random
t=0
def tp():
  global t
  x = random.random()
  y = random.random()
  z = random.random()
  if (x+y)+z!=x+(y+z):
  #if abs((x+y)+z)-(x+(y+z)) >= 0.000000000000001:
    print(f"False: {x}, {y}, {z}")
    t=t+1

for i in range(1000):
  tp()

print({1-t/1000})