import numpy
import random
random.seed(100)

images_list = []

for i in range(4):
    value_list = [round(random.uniform(0.05,1.0),2), i]
    images_list.append(value_list)


for item in images_list:
    print(item)

