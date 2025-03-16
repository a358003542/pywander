import pandas as pd
import torch
from torch import nn as nn


def get_torch_device_type():
    device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
    print(f"Using {device} device")
    return device


class NeuralNetwork(nn.Module):
    """
    神经网络
    """
    device = get_torch_device_type()

    def __init__(self, *args, **kwargs):
        super().__init__()

        if kwargs.get('in_features'):
            self.in_features = kwargs.get('in_features')
        if kwargs.get('out_features'):
            self.out_features = kwargs.get('out_features')

        # 一般只有一个模型 默认存储的模型名就是model
        self.model = None
        # 损失函数
        self.loss_function = None
        # 优化器
        self.optimizer = None

        # 训练计数 以优化器step为准
        self.train_counter = 0
        self.train_progress = []

    def forward(self, inputs):
        return self.model(inputs)

    def to_device(self):
        self.to(self.device)


    def train_batch2(self, dataloader):
        """
        通过dataloader批次训练

        批次训练更有效率，但就这个简单的网络加上这里入门级别的配置造成效果不是很好，暂时这里先转成单个训练模式
        """
        self.train_counter = 0
        size = len(dataloader.dataset)
        self.model.train()

        for batch, (inputs_batch, targets_batch) in enumerate(dataloader):
            for inputs, targets in zip(inputs_batch, targets_batch):

                inputs, targets = inputs.to(self.device), targets.to(self.device)

                outputs = self.forward(inputs)
                loss = self.loss_function(outputs, targets)

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                self.train_counter += 1
                if self.train_counter % 20 == 0:
                    self.train_progress.append(loss.item())

                if self.train_counter % 3000 == 0:
                    print(f"loss: {loss.item():>7f}  [{self.train_counter:>5d}/{size:>5d}]")

    def train_batch(self, dataloader):
        """
        通过dataloader批次训练

        批次训练更有效率，但就这个简单的网络加上这里入门级别的配置造成效果不是很好，暂时这里先转成单个训练模式
        """
        self.train_counter = 0
        size = len(dataloader.dataset)
        self.model.train()

        for batch, (inputs_batch, targets_batch) in enumerate(dataloader):
            inputs, targets = inputs_batch.to(self.device), targets_batch.to(self.device)

            outputs = self.forward(inputs)
            loss = self.loss_function(outputs, targets)

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

            self.train_counter += 1
            if self.train_counter % 5 == 0:
                self.train_progress.append(loss.item())

            if batch % 100 == 0:
                loss = loss.item()
                current = (batch + 1) * len(inputs_batch)
                print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

    def test_batch(self, dataloader):
        """
        通过dataloader批次测试
        """
        size = len(dataloader.dataset)
        num_batches = len(dataloader)
        self.model.eval()

        test_loss, correct = 0, 0
        with torch.no_grad():
            for inputs, targets in dataloader:
                inputs, targets = inputs.to(self.device), targets.to(self.device)

                outputs = self.forward(inputs)
                test_loss += self.loss_function(outputs, targets).item()

                predicted_indices = torch.argmax(outputs, dim=1)
                target_indices = torch.argmax(targets, dim=1)

                correct_count = (predicted_indices == target_indices).sum().item()
                correct += correct_count

        test_loss /= num_batches
        correct /= size
        print(f"Test Error: \n Accuracy: {(100 * correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")

    def plot_progress(self):
        df = pd.DataFrame(self.train_progress, columns=['loss'])
        df.plot(ylim=(0, 1.0), figsize=(16, 8), alpha=0.1, marker='.', grid=True, yticks=(0, 0.25, 0.5))
