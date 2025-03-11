# library
import matplotlib.pyplot as plt
import numpy as np
import time

def generateRefBarPlot():
    # Create bars
    barWidth = 0.85

    np.random.seed(int(time.time()))
    bars1 = [6, 6, 2]
    bars2 = [8, 4, 6]
    bars3 = [2, 3, 3.5, 5, 2, 2]
    bars4 = bars1 + bars2 + bars3  # for adding text
    
    # The X position of bars
    r1 = [1+2,5+2,9+2]
    r2 = [2+2,6+2,10+2]
    r3 = [3,4,7,8,11,12]
    r3 = [x-2 for x in r3]
    r4 = r1 + r2 + r3

    # plt.figure(figsize=(10, 5))
    plt.bar(r1, bars1, width = barWidth, color = (0.55, 0, 0.0, 1), label='Alone')
    plt.bar(r2, bars2, width = barWidth, color = (0, 0.39, 0, 1), label='With Himself')
    plt.bar(r3, bars3, width = barWidth, color = (0.3,0.9,0.4, 1), label='With other genotype')

    # Create legend
    plt.legend()
    
    # Text below each barplot with a rotation at 90°
    plt.xticks([r + barWidth for r in range(len(r4))], ['DD', 'with himself', 'with DC', 'with Silur', 'DC', 'with himself', 'with DD', 'with Silur', 'Silur', 'with himself', 'with DD', 'with DC'], rotation=90)
    
    # Create labels
    label = ['n = 6', 'n = 25', 'n = 13', 'n = 36', 'n = 30', 'n = 11', 'n = 16', 'n = 37', 'n = 14', 'n = 4', 'n = 31', 'n = 34']

    # Text on the top of each bar
    for i in range(len(r4)):
        plt.text(x = r4[i]-0.5 , y = bars4[i]+0.1, s = label[i], size = 6)

    # Adjust the margins
    plt.subplots_adjust(bottom= 0.2, top = 0.98)
    
    # Show graphic
    # plt.tight_layout()
    plt.savefig('./Prototype/backend/Algorithm/examples/barplot_dpi100_width8.png', dpi=100)
    plt.show()

def generateRefBarPlot_2Groups():
    # Sample data
    categories = ['A', 'B', 'C', 'D', 'E']
    # randomly generate numbers within a range
    random_numbers = np.random.randint(1, 30, size=(5, 2))
    values_group1 = random_numbers[:, 0]
    values_group2 = random_numbers[:, 1]

    # Define the width of the bars
    bar_width = 0.4
    x = np.arange(len(categories))  # The label locations

    # Create the figure and axis
    plt.figure(figsize=(8, 5))

    # Plot bars for both groups
    plt.bar(x - bar_width/2 - 0.01, values_group1, width=bar_width, label='Group 1')
    plt.bar(x + bar_width/2 + 0.01, values_group2, width=bar_width, label='Group 2')

    # Add labels and title
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Bar Plot with Two Groups')
    plt.xticks(x, categories)  # Set category labels on x-axis
    plt.legend()

    # Show the plot
    plt.savefig('./Prototype/backend/Algorithm/examples/barplot_2groups_dpi200.png', dpi=200)
    plt.show()


def generateRefPieChart():    
    plt.rcParams["figure.figsize"] = (20,5)
    # create random data
    names='groupA', 'groupB', 'groupC', 'groupD',
    values=[12, 11, 3, 30]

    # Label distance: gives the space between labels and the center of the pie
    plt.pie(values, labels=names, labeldistance=1.15, colors=[(1, 0, 0.0, 1), (0, 1, 0, 1), (0,0,1, 1), (1,1,0, 1)])
            # wedgeprops = { 'linewidth' : 0, 'edgecolor' : 'white' }
    plt.tight_layout()
    plt.savefig('./Prototype/backend/Algorithm/piechart_raw.png', dpi=150)
    plt.show()

if __name__ == '__main__':
    generateRefBarPlot()
    # generateRefBarPlot_2Groups()
    # generateRefPieChart()