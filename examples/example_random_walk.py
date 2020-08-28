#!/usr/bin/env python
# -*-coding:utf-8-*-

from my_python_module.algorithm.random_walk import drunk_test, UsualDrunk
from my_python_module.helper.matplotlib_helper import polyfit_plot
import matplotlib.pyplot as plt

num_steps_batch = list(range(100, 10000, 100))
data = drunk_test(num_steps_batch, 100, UsualDrunk)

fig, ax = plt.subplots()
polyfit_plot(ax, num_steps_batch, data)
