import pandas as pd
import numpy as np
from data import data
import orchestrator1 as orch1
import orchestrator2 as orch2


def main():
    df1 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
    df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])
    num = 3

    data = data.Data(df1, df2, num)
    
    orch1(data)
    print(data)

    data2 = data.Data(df1, df2, num)

    orch2(data2)
    print(data2)
    
if __name__ == '__main__':
    main();

