import matplotlib.pyplot as plt
import numpy as np
import random

def combine(dict_1,dict_2):
    my_dict={}
    for key in dict_1.keys():
        my_dict[key]=(dict_1[key],dict_2[key])
    return my_dict

def plot_triangles(triangles, filename):
    plt.clf()
    for triangle in triangles:
        x = [point[0] for point in triangle]
        y = [point[1] for point in triangle]
        plt.plot(x + [x[0]], y + [y[0]], 'k-')
    # plt.title('Mesh Structure',fontweight='bold')
    plt.xlabel('x (meter)',fontsize=24)
    plt.ylabel('y (meter)',fontsize=24)

    plt.axis('equal')  # ensures that x and y scales are equal
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    # print(f"Plot saved as {filename}")

# example dictionary
def velo_plot(velocity_dict,obj,l,b):
    plt.clf()

    # calculate 20% of the total number of keys in the dictionary
    n = len(velocity_dict)
    n_20_percent = int(n * 1)

    # randomly select that many keys from the dictionary
    selected_keys = random.sample(list(velocity_dict.keys()), n_20_percent)

    # create the plot
    plt.xlabel('x (meter)')
    plt.ylabel('y (meter)')
    plt.xlim(0, l)
    plt.ylim(0, b)

    # create a list of colors for the arrows
    colors = plt.cm.rainbow(np.linspace(0, 1, len(selected_keys)))

    # iterate over the selected keys and plot the velocity vectors
    for i, key in enumerate(selected_keys):
        vx, vy = velocity_dict[key]
        scaling_factor = 0.00005
        color = colors[i]
        plt.arrow(key[0], key[1], vx*scaling_factor, vy*scaling_factor, head_width=0.01, head_length=0.05, fc=color, ec=color)

    plt.savefig('velo_plot_png/'+'vel_'+str(obj)+'.png')



