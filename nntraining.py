import pandas as pd
import numpy as np
import torch

y_col = ["optimal_play"]

tictactoe_data_filepath = "tree_exported.txt"

df_tictactoe = pd.read_csv(tictactoe_data_filepath)

X_col = ["S" + str(i) for i in range(9)]
X = df_tictactoe[X_col].values

y = df_tictactoe[y_col].values
y[y == " None"] = -1

y = y.astype(np.int)

valid_idxs = y != -1
valid_idxs = valid_idxs.reshape((-1, ))

y = y[valid_idxs]
X = X[valid_idxs, :]

print(X.shape)
print(y.shape)
print(X[0:3, :])
print(y[0:3, 0])


