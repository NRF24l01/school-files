import torch
from torch import nn, optim
import torch.nn.functional as F
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

class Net(nn.Module):
    def __init__(self,neyrons):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(1, neyrons)
        self.fc2 = nn.Linear(neyrons, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

#import torch
#from torch import nn, optim
#import torch.nn.functional as F
#import numpy as пр

#import matplotlib
#import matplotlib.pyplot as plt

#import GPUtil
#from tabulate import tabulate

#class Net(nn.Module):
#    def __init__(self,neyrons):
#        super(Net, self).__init__()
#        self.fc1 = nn.Linear(1, neyrons)
#        self.fc2 = nn.Linear(neyrons, 1)

#    def forward(self, x):
#        x = F.relu(self.fc1(x))
#        x = self.fc2(x)
#        return x

DEVICE = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu") #Выбо устройства
print(DEVICE)
net = Net(200)     #Количество нейронов
net.to(DEVICE)
optimizer = optim.Adam(net.parameters(), lr=0.001)     #Точность
net.train()
epohs = 50000    #Количество эпох 50000


def loss(pred, target):
    squares = (pred - target) ** 2
    return squares.mean()                   #Функция возведения в степень


#
x_train = torch.rand(100)
x_train = x_train * 20.0 - 10.0
y_train = torch.cos(x_train)
x_train.unsqueeze_(1)
y_train.unsqueeze_(1)

#Записываем в степень
x_train = x_train.to(DEVICE)
y_train = y_train.to(DEVICE)


for epoch_index in range(epohs):
#    gpus = GPUtil.getGPUs()
#    gpus_list = []
#    for gpu in gpus:
#        gpu_load = f'{gpu.load*100}%'
#        print(gpu_load)
#        gpu_used_memory = f'{gpu.memoryUsed}MB'
#        print(gpu_used_memory)
#        gpu_temp = f'{gpu.temperature}'
#        print(gpu_temp)
#    print(" ")
    optimizer.zero_grad()
    y_pred = net(x_train)
    #print(y_pred.shape,y_train.shape)
    loss_val = loss(y_pred, y_train)
    #print(epoch_index, loss_val)
    loss_val.backward()
    optimizer.step()
    print(epoch_index)


x_test = torch.rand(100000)
x_test.unsqueeze_(1)
x_test = x_test * 20.0 - 10.0
x_test = x_test.to(DEVICE)
y_pred = net.forward(x_test)
plt.plot(x_test.detach().cpu().numpy(), y_pred.detach().cpu().numpy(), 'o')
plt.xlabel('$x$')
plt.ylabel('$y$')