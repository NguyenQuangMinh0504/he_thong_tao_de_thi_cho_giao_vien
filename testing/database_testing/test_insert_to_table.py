import pandas as pd
import numpy as np

x = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(x)
x.loc[-1] = ["a", "b", "c"]
x.index += 1
x.sort_index(inplace=True)
x.loc[-1] = ["c", "d", "e"]
print(x)