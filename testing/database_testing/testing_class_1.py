import pandas as pd
import numpy as np

x = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

def foo_1():
    x.drop(1, inplace=True)

def foo_2():
    print(x)

