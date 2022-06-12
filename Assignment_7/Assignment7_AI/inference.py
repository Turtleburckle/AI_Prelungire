# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:20:51 2021

@author: tudor
"""

import torch
import torch.nn.functional as F
import math
import myModel
import matplotlib.pyplot as plt



# we load the model

filepath = "myNet.pt"
ann = myModel.Net()

ann.load_state_dict(torch.load(filepath))
ann.eval()

# visualise the parameters for the ann (aka weights and biases)
# for name, param in ann.named_parameters():
#     if param.requires_grad:
#         print (name, param.data)
matrix = []
with open("myDataset.csv", "r") as file:
    n = int(file.readline()[:-1])
    for _ in range(n):
        matrix.append(tuple(map(float, file.readline().strip().split(","))))

ans_matrix = []
for vector in matrix:
    ans_matrix.append(math.sin(vector[0] + vector[1] / math.pi))

x = torch.Tensor(matrix)
y = torch.unsqueeze(torch.Tensor(ans_matrix), dim=1)

ans = ann(x)
data = []
for i, y in enumerate(zip(ans, y)):
    data.append((i, y[0].tolist()[0] - y[1].tolist()[0]))
for val in data:
    plt.scatter(val[0], val[1], color="black")
plt.show()


x = float(input("x = "))
y = float(input("y = "))
x = torch.tensor([x, y])
print(ann(x).tolist()[0])