import json
import matplotlib.pyplot as plt
import numpy as np

data = json.load(open('cats.json'))

#pprint(data)
cat_weight = []
for cat in data:
    if cat['sex'] == 'F':
        print cat
        cat_weight.append(cat['bodyWeight'])

plt.hist(cat_weight, bins='auto')
plt.title("Histogram of cat weights")
plt.show()
