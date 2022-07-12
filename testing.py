import pandas as pd
if __name__ == '__main__':
    a = pd.read_csv("./database/Question/Question.csv")
    print(a)
    b = a.query("Type == 'trac_nghiem'")
    print(b)