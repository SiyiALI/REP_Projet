import argparse
import random

def property_holds(min_bound: float, max_bound: float) -> bool:
  """
  Returns true if (x+y)+z==x+(y+z)
  """
  x = random.uniform(min_bound, max_bound)
  y = random.uniform(min_bound, max_bound)
  z = random.uniform(min_bound, max_bound)

  return (x + y) + z == x + (y + z)

parser = argparse.ArgumentParser()
parser.add_argument('--min', type=float, required=True)
parser.add_argument('--max', type=float, required=True)
parser.add_argument('--steps', type=int, required=True)

args = parser.parse_args()
min = args.min
max = args.max
steps = args.steps

true_counter = 0
for _ in range(steps):
  if property_holds(min, max):
    true_counter += 1

with open("answer_associativity.txt", "w+") as file:
  file.write(str(true_counter/steps))
