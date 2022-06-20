import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class DriverExplorer:
    def __init__(self, data):
        self.frame = data
        self.correlation = self.frame.corr()

    def show_heatmap(self):
        sns.heatmap(self.correlation)
        plt.show()

    def show_countplot(self, column):
        plt.figure(figsize = (10, 8))
        sns.countplot(x = self.frame[column])
        plt.show()

    def show_histogram(self, column):
        plt.figure(figsize=(10, 8))
        sns.histplot(self.frame[column])
        plt.show()

