import torch
from torch import nn as nn

from pywander.utils.plot_utils import line_plot


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
        for module in self.children():
            module.to(self.device)

        self.to(self.device)

    def train_one(self, inputs, targets):
        """
        单个训练模式
        """
        self.train()

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
            print(f"trained by: {self.__class__.__name__} "
                  f"loss: {loss.item():>7f}  train_counter: {self.train_counter:>5d}")

        return loss.item()

    def reset_train_counter(self):
        """
        主要是针对train_one单个训练模式 批次训练流程是在外面控制的
        """
        self.train_counter = 0

    def train_batch2(self, dataloader):
        """
        通过dataloader批次训练

        某些情况下可能需要强制转为单个训练模式
        """
        self.train_counter = 0
        size = len(dataloader.dataset)
        self.train()

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

        批次训练更有效率
        """
        self.train_counter = 0
        size = len(dataloader.dataset)
        self.train()

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
        self.eval()

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

    def plot_progress(self, ax=None, **kwargs):
        if ax is None:
            import matplotlib.pyplot as plt
            ax = plt.gca()

        line_plot(ax, y_values=self.train_progress, marker='.', y_lim=(0, 1.0), y_label='loss', **kwargs)
