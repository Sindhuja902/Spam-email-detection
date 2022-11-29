import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import sys

def view(rlist):
    height=rlist
    bars = ('KNN','NB','SVM')
    y_pos = np.arange(len(bars))
    plt.bar(y_pos, height, color=['orange','green','blue'])
    plt.xticks(y_pos, bars)
    plt.xlabel('Algorithm Metrics')
    plt.ylabel('Accuracy Score')
    plt.title('Algorithms Performance')
    plt.show()


