from functools import reduce
res = [[1,2,3],[1,2],[1,4,5,6,7]]

# method -1
print(len(res))
ans = reduce(lambda x, y : x + y, res)
print(ans)

# method -2
import itertools

sol = list(itertools.chain(*res))
print(sol)

# list comprehension

my_list = [x for y in res for x in y]
print(my_list)


#########

import numpy as np
a = [10,9,8,6,4,2]
a = np.array(a)
res = a[[3,1,2]]
print(res)
