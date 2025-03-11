from pywander.datasets import load_mnist_train_data, load_mnist_csv_data, get_datasets_path


def test_load_mnist_train_data():
    data = load_mnist_train_data(line_count=1)
    data = list(data)

    assert data[0][0] == 5
    assert len(data[0][1]) == 28*28



