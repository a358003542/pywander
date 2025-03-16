import torch
import torch.nn as nn
import random

import pandas

import matplotlib.pyplot as plt


def generate_real():
    real_data = torch.FloatTensor([
        random.uniform(0.8, 1.0),
        random.uniform(0.0, 0.2),
        random.uniform(0.8, 1.0),
        random.uniform(0.8, 0.2)
    ])
    return real_data

def generate_random(size):
    random_data = torch.rand(size)
    return random_data


from pywander.neural_network.general import NeuralNetwork

class Sensor(NeuralNetwork):
    """
    一般感知器
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Operator(NeuralNetwork):
    """
    一般行动器
    """

class ReplacerO(NeuralNetwork):
    """
    GAN网络架构 替换器O 存储的是知觉信息 实现 Op1->Op2

    复杂网络架构的训练首先要判断谁对谁错，只有错的那些网络节点才会被训练
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ReplacerS(NeuralNetwork):
    """
    替换器S 存储的是行动信息 实现S1-> S2
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(4, 3),
            nn.Sigmoid(),
            nn.Linear(3,1),
            nn.Sigmoid()
        )

        self.loss_function = nn.MSELoss()
        self.optimiser = torch.optim.SGD(self.parameters(), lr=0.01)

        self.counter = 0
        self.progress = []

    def forward(self, inputs):
        return self.model(inputs)


    def train_one(self, inputs, targets):
        """
        训练一次
        """
        self.model.train()

        inputs, targets = inputs.to(self.device), targets.to(self.device)

        outputs = self.forward(inputs)
        loss = self.loss_function(outputs, targets)

        # increase counter and accumulate error every 10
        self.counter += 1
        if self.counter % 10 == 0:
            self.progress.append(loss.item())

        if self.counter % 10000 == 0:
            print("counter = ", self.counter)

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return loss.item()

    def to_device(self):
        self.to(self.device)

    def plot_progress(self):
        df = pandas.DataFrame(self.progress, columns=['loss'])
        df.plot(ylim=(0, 1.0), figsize=(16,8), alpha=0.1, marker='.', grid=True, yticks=(0, 0.25, 0.5))



if __name__ == '__main__':
    D = Discriminator()

    for i in range(10000):
        # real data
        D.train_one(generate_real(), torch.FloatTensor([1.0]))
        # fake data
        D.train_one(generate_random(4), torch.FloatTensor([0.0]))
        pass