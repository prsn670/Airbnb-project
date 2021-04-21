import matplotlib.pyplot as plt
import numpy as np

def plot_bar_chart(variables, delta_list):

    selected_deltas = []
    associated_feature = []
    for delta, variable in zip(delta_list, variables):
        if delta <= -0.01 or delta >= 0.002:
            selected_deltas.append(delta)
            associated_feature.append(variable)

    plt.rcdefaults
    fig, ax = plt.subplots()
    y_pos = np.arange(len(associated_feature))
    ax.barh(y_pos, selected_deltas)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(associated_feature)
    ax.set_xlabel('Change in R2 score')
    ax.set_ylabel('Dropped Feature')
    ax.set_title('R2 delta versus Feature')
    plt.setp(ax.get_yticklabels(), rotation=30, horizontalalignment='right')
    for index, value in enumerate(selected_deltas):
        plt.text(value, index, str(value))
    plt.show()
