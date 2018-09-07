import tempfile

import numpy as np

# a = np.array([1., 2., 3.])
# b = np.array(range(4, 10))
# c = np.random.uniform(size=(5, 2))
# print(c)

# l1 = [1,2,3]
# l2 = [1,2,3,4]
# l3 = [1,2,3,4,5]
#
# z = zip(l1,l2)
# print(dict(z))

tmp = np.loadtxt('C:\\Users\\HYGPC180709010\\.keras\\datasets\\iris_training.csv', dtype=np.str, delimiter=',')
# print(tmp)
data = tmp[1:, 0:-1].astype(np.float)
# print(data)
label = tmp[1:, -1].astype(np.int)
print(label)

# '6.4' '2.8' '5.6' '2.2' '2'