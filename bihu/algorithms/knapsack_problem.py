#!/usr/bin/env python
# -*-coding:utf-8-*-

"""

实用pandas的dataframe结构是为了更清晰的表达


"""

import pandas as pd


class Knapsack(object):
    def __init__(self, capacity, items=None):
        self.capacity = capacity
        self.items = [] if items is None else items
        self.freespace = self.capacity

    def add_item(self, item):
        if self.freespace - item.weight >= 0:
            self.freespace -= item.weight
            self.items.append(item)
            return True
        else:
            return False

    def all_items_value(self):
        value = 0
        for item in self.items:
            value += item.value
        return value

    def __repr__(self):
        return '<Knapsack: {0}>'.format(self.items)


class Item(object):
    def __init__(self, name, value, weight):
        self.value = value
        self.weight = weight
        self.name = name

    def __repr__(self):
        return '<Item: {0}>'.format(self.name)

    def __eq__(self, other):
        if self.name == other.name and self.value == other.value and self.weight == other.weight:
            return True
        else:
            return False



def greedy_algorithm(knapsack, items):
    """
    贪婪法求解
    :return:
    """
    items_copy = items.copy()
    found = True

    while found:
        max_value = 0
        choosed_item = None
        for item in items_copy:
            if item.value > max_value:
                choosed_item = item
                max_value = choosed_item.value

        if knapsack.add_item(choosed_item):
            found = True
            items_copy.remove(choosed_item)
        else:
            found = False
    return knapsack


def dynamic_programming(knapsack, items):
    """
    动态规划法求解
    :return:
    """
    len_i = len(items)
    len_j = knapsack.freespace

    df = pd.DataFrame(index=[item.name for item in items], columns=range(1, len_j + 1))
    for i in range(len_i):
        for j in range(1, len_j + 1):
            if i == 0:  # 第一行
                item = items[i]
                test_knapsack = Knapsack(capacity=j)
                test_knapsack.add_item(item)
                df.iloc[i][j] = test_knapsack
            else:
                upper_item_value = df.iloc[i - 1][j].all_items_value()
                rightnow_item_value = items[i].value

                if j - items[i].weight == 0:
                    check_value = rightnow_item_value
                elif j - items[i].weight >= 1:
                    check_value = rightnow_item_value + df.iloc[i - 1][j - items[i].weight].all_items_value()
                else:
                    check_value = 0

                test_knapsack = Knapsack(capacity=j)
                if upper_item_value >= check_value:  # 和上面的背包状态一样
                    for item in df.iloc[i - 1][j].items:
                        test_knapsack.add_item(item)
                    df.iloc[i][j] = test_knapsack
                else:
                    if j - items[i].weight == 0:
                        test_knapsack.add_item(items[i])
                    else:
                        test_knapsack.add_item(items[i])
                        for item in df.iloc[i - 1][j - items[i].weight].items:
                            test_knapsack.add_item(item)
                    df.iloc[i][j] = test_knapsack
    print(df)
    return df.iloc[len_i - 1][len_j]

