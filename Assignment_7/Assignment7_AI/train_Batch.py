import torch
import math
import torch.nn.functional as F
import tqdm
import matplotlib.pyplot as plt
import numpy as np

import myModel

trainig_percentage = 0.8

epochs = 100

matrix = []

# Read the data from the file
with open("myDataset.csv", "r") as file:
    n = int(file.readline()[:-1])
    for i in range(n):
        matrix.append(tuple(map(float, file.readline().strip().split(","))))

# How much to cut off from the matrix
cutoff = int(len(matrix) * trainig_percentage)

# [ matrix * cutoff * test_matrix]
test_matrix = matrix[cutoff:]

matrix = matrix[:cutoff]

# Generate the Matrix of the results (of the matrix)
ans_matrix = []

for vector in matrix:
    ans_matrix.append(math.sin(vector[0] + vector[1] / math.pi))

# Generate the Matrix of the results (of the test matrix)
ans_test_matrix = []

for vector in test_matrix:
    ans_test_matrix.append(math.sin(vector[0] + vector[1] / math.pi))

# Creates a one-dimensional tensor of size 100 whose values are evenly spaced
# from -1 to 1, inclusive, and is placing the values in a tensor like
# so x = [ [-1], [-0.98], ..., [0.98]. 1]
x = torch.Tensor(matrix)

test_x = torch.Tensor(test_matrix)

# Returns a new tensor with a dimension of size one inserted at the specified position.
# The returned tensor shares the same underlying data with this tensor.
y = torch.unsqueeze(torch.Tensor(ans_matrix), dim=1)

test_y = torch.unsqueeze(torch.Tensor(ans_test_matrix), dim=1)

# we create the ANN
ann = myModel.Net()

# we set up the lossFunction as the mean square error
lossFunction = torch.nn.MSELoss()

# we use an optimizer that implements stochastic gradient descent
# (find the model parameters that correspond to the best fit between predicted and actual outputs)
#  Adam combines the best properties of the AdaGrad and RMSProp algorithms to provide an optimization
#  algorithm that can handle sparse gradients on noisy problems.
optimizer_batch = torch.optim.Adam(ann.parameters())

# we memorize the losses for some graphics
loss_list = []
avg_loss_list = []

# we set up the environment for training in batches  
batch_size = 1
n_batches = int(len(x) / batch_size)
print(f"Running {n_batches} batches")

for epoch in tqdm.trange(epochs):
    for batch in range(n_batches):
        # we prepare the current batch  -- please observe the slicing for tensors
        batch_x, batch_y = x[batch * batch_size:(batch + 1) * batch_size, ], \
                           y[batch * batch_size:(batch + 1) * batch_size, ]

        # we compute the output for this batch
        prediction = ann(batch_x)

        # we compute the loss for this batch
        loss = lossFunction(prediction, batch_y)

        # we set up the gradients for the weights to zero (important in pytorch)
        optimizer_batch.zero_grad()

        # we compute automatically the variation for each weight (and bias) of the network
        loss.backward()

        # we compute the new values for the weights
        optimizer_batch.step()

        # we print the loss for all the dataset for each 10th epoch
    # we save it for graphics
    loss = lossFunction(ann(test_x), test_y)
    loss_list.append(loss.tolist())
    if epoch % 100 == 99:
        print('\repoch: {}\tLoss =  {:.5f}'.format(epoch, loss))

    # Specify a path
filepath = "myNet.pt"

# save the model to file
torch.save(ann.state_dict(), filepath)

# visualise the parameters for the ann (aka weights and biases)
# for name, param in ann.named_parameters():
#     if param.requires_grad:
#         print (name, param.data)
plt.plot(loss_list)
plt.ylim((0, None))
plt.show()
