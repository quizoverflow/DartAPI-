from tool import *
import time
import random

from tqdm import tqdm


nums = []
for i in range(10000000):
	nums.append(i)

for i in tqdm(nums):
	pass
print("fin")