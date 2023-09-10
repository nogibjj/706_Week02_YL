from descriptive import gen_df
import numpy as np

if __name__ == "__main__":
    X = np.random.randint(0, 20)
    res = gen_df(X)
    print(res)