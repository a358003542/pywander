import torch
import torch.nn as nn


def get_torch_device_type():
    device = torch.accelerator.current_accelerator().type if torch.accelerator.is_available() else "cpu"
    print(f"Using {device} device")
    return device


class SimpleMLP(nn.Module):
    """
    单隐藏层感知机
    """
    device = get_torch_device_type()

    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(28 * 28, 200),
            nn.Sigmoid(),
            nn.Linear(200, 10),
            nn.Sigmoid()
        )

        self.loss_function = nn.MSELoss()
        self.optimizer = torch.optim.SGD(self.parameters(), lr=0.01)

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

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return loss.item()

    def to_device(self):
        self.to(self.device)

    def train_batch(self, dataloader):
        """
        通过dataloader批次训练

        批次训练更有效率，但就这个简单的网络加上这里入门级别的配置造成效果不是很好，暂时这里先转成单个训练模式
        """
        size = len(dataloader.dataset)
        self.model.train()
        loss = 0

        for batch, (inputs_batch, targets_batch) in enumerate(dataloader):
            for inputs, targets in zip(inputs_batch, targets_batch):
                loss = self.train_one(inputs, targets)

            if batch % 100 == 0:
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


class SimpleMLP2(nn.Module):
    """
    对简单单隐藏层感知机进行一些改良
    BCELoss 更适合分类任务 只能处理0-1的数值 需要加一个Sigmoid层
    线性整流函数  ReLU
    带泄露线性整流函数 Leaky ReLU 比ReLU在负数上表现稍好
    LayerNorm 归一化层 在进入下一层神经网络进行归一化处理可以提升网络性能
    Adam优化器 会自适应调整学习率 增加动量来避免陷入局部最小值 表现一般比SGD好
    批次训练提升训练效率 多次训练
    """
    device = get_torch_device_type()

    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(28 * 28, 200),
            nn.LeakyReLU(0.02),
            nn.LayerNorm(200),
            nn.Linear(200, 10),
            nn.Sigmoid()
        )

        self.loss_function = nn.BCELoss()
        self.optimizer = torch.optim.Adam(self.parameters())

    def forward(self, inputs):
        return self.model(inputs)

    def to_device(self):
        self.to(self.device)

    def train_batch(self, dataloader):
        """
        通过dataloader批次训练

        批次训练更有效率，但就这个简单的网络加上这里入门级别的配置造成效果不是很好，暂时这里先转成单个训练模式
        """
        size = len(dataloader.dataset)
        self.model.train()

        for batch, (inputs_batch, targets_batch) in enumerate(dataloader):
            inputs, targets = inputs_batch.to(self.device), targets_batch.to(self.device)

            outputs = self.forward(inputs)
            loss = self.loss_function(outputs, targets)

            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

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


if __name__ == '__main__':
    def train_simple_mlp():
        from pywander.datasets import MnistDataset

        training_data = MnistDataset(train=True)
        from torch.utils.data import DataLoader

        batch_size = 16
        train_dataloader = DataLoader(training_data, batch_size=batch_size)

        model = SimpleMLP()
        model.to_device()

        epochs = 3
        for e in range(epochs):
            model.train_batch(train_dataloader)

        from pywander.models import save_model, load_model

        model = save_model(model, 'mnist', 'simple_mlp.pkl')


    def test_simple_mlp():
        from pywander.datasets import MnistDataset

        test_data = MnistDataset(train=False)
        from torch.utils.data import DataLoader
        batch_size = 16
        test_dataloader = DataLoader(test_data, batch_size=batch_size)

        from pywander.models import save_model, load_model
        model = load_model('mnist', 'simple_mlp.pkl')

        model.test_batch(test_dataloader)


    # train_simple_mlp()
    # test_simple_mlp()

    def train_simple_mlp2():
        from pywander.datasets import MnistDataset

        training_data = MnistDataset(train=True)
        from torch.utils.data import DataLoader

        batch_size = 32
        train_dataloader = DataLoader(training_data, batch_size=batch_size, shuffle=True)

        model = SimpleMLP2()
        model.to_device()

        epochs = 5
        for e in range(epochs):
            model.train_batch(train_dataloader)

        from pywander.models import save_model, load_model

        model = save_model(model, 'mnist', 'simple_mlp2.pkl')


    def test_simple_mlp2():
        from pywander.datasets import MnistDataset

        test_data = MnistDataset(train=False)
        from torch.utils.data import DataLoader
        batch_size = 32
        test_dataloader = DataLoader(test_data, batch_size=batch_size, shuffle=True)

        from pywander.models import save_model, load_model
        model = load_model('mnist', 'simple_mlp2.pkl')

        model.test_batch(test_dataloader)


    train_simple_mlp2()
    test_simple_mlp2()
