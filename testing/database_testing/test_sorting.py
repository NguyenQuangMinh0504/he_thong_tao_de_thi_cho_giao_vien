import pandas as pd
table = pd.read_csv("./something.csv")
print(table)
print(table.index)
# table.sort_values(by="question_id", inplace=True)
# print(table)
# table = pd.concat([table, pd.Series([2, "something2"])], ignore_index=True)
# print(table)
table.iloc[-1] = [2, "something2"]
print(table.index)
table.index += 1
print(table.index)
print(table)