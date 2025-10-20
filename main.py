import random
import numpy as np
t=0
def tp():
  global t
  x = np.float32(random.random())
  y = np.float32(random.random())
  z = np.float32(random.random())
  if (x+y)+z!=x+(y+z):
  #if abs((x+y)+z)-(x+(y+z)) >= 0.000000000000001:
    #print(f"False: {x}, {y}, {z}")
    t=t+1

for i in range(1000):
  tp()

with open("answer_associativity.txt", "w+") as file:
  file.write(str(1-t/1000))

#print({1-t/1000})
