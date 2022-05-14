import pandas as pd
import numpy as np

x = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
x.to_excel("./something.xlsx", index=False)