import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import pickle

lr = 0.01
momentum = 0.5
epochs = 20
device = "cpu"
log_interval = 100

class TictactoeNet(nn.Module):
    #defines convolutional and dropout layers as part of NN
    def __init__(self):
        super(TictactoeNet, self).__init__()
        self.fc0 = nn.Linear(3 * 3, 9)
        self.fc1 = nn.Linear(9, 100)
        self.fc2 = nn.Linear(100, 100)
        self.fc3 = nn.Linear(100, 100)
        self.fc4 = nn.Linear(100, 3 * 3)
    #sets up more layers (to be used)
    def forward(self, x):
        #our input x is of shape (batch, 3 * 3)
        x = F.relu(self.fc0(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = F.relu(self.fc4(x))
        return F.log_softmax(x, dim = 1)

def train(model, device, X, y, optimizer, epoch):
    #tells model its training time so layers like dropout can behave acordingly;
    model.train()
    #for each batch in training dataset ready to be used:
    batch_size = 1
    for idx in range(int(X.shape[0]/batch_size)):
        begin = idx * batch_size
        data = X[begin:begin + batch_size, :]
        target = y[begin : begin + batch_size]
        target = target.reshape((target.shape[0], ))
        #throw it on cpu or gpu
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        #forward pass
        output = model(data)
        #loss function
        loss = F.nll_loss(output, target)
        #backwards propagation
        loss.backward()
        #optimizes all layers
        optimizer.step()
        #logs every 11th batch index (if log_interval == 11)
        if idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, idx * len(data), X.shape[0],
                       100. * idx / X.shape[0], loss.item()))

def test(model, device, X, y):
    #for each batch in training dataset ready to be used:
    batch_size = 250
    num_corrects = 0
    for idx in range(int(X.shape[0]/batch_size)):
        begin = idx * batch_size
        data = X[begin:begin + batch_size, :]
        target = y[begin : begin + batch_size]
        target = target.reshape((target.shape[0], ))
        #throw it on cpu or gpu
        data, target = data.to(device), target.to(device)
        #forward pass
        output = model(data)
        output = output.cpu().detach().numpy()
        y_pred = np.argmax(output, axis=1).flatten()
        y_true = y_torch[begin:begin + batch_size].cpu().detach().numpy().flatten()
        correct = y_pred == y_true
        num_corrects += np.sum(correct)
        #logs every 11th batch index (if log_interval == 11)
        if idx % log_interval == 0:
            print('Test: [{}/{} ({:.0f}%)]'.format(
                 idx * len(data), X.shape[0],
                       100. * idx / X.shape[0]))
    return num_corrects

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

Y = np.zeros((y.shape[0], 9))

# for x_index in range(Y.shape[0]):
#     Y[x_index, y[x_index]] = 1

X_torch = torch.tensor(X).float()
y_torch = torch.tensor(y).long()
# Y_torch = torch.tensor(Y).long()
load_model = False
if load_model:
    model = pickle.load(open("TictactoeNet.p", "rb"))
else:
    model = TictactoeNet().to(device)
    output_y = model.forward(X_torch)

    optimizer = optim.Adam(model.parameters())
    #trains & tests each epoch
    for epoch in range(1, epochs + 1):
        train(model, device, X_torch, y_torch, optimizer, epoch)


    pickle.dump(model, open("TictactoeNet.p", "wb"))

num_corrects = test(model, device, X_torch, y_torch)
print(num_corrects/X_torch.shape[0])