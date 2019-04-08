#!/usr/bin/env python
# -*-coding:utf-8-*-

from algorithms.random_walk import drunk_test, UsualDrunk
from utils.plot_utils import polyfit_plot
import matplotlib.pyplot as plt

num_steps_batch = list(range(100, 10000, 100))
data = drunk_test(num_steps_batch, 100, UsualDrunk)

fig, ax = plt.subplots()
polyfit_plot(ax, num_steps_batch, data)
