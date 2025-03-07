# library
import matplotlib.pyplot as plt
import numpy as np

def generateRefBarPlot():
    # Create bars
    barWidth = 0.9
    bars1 = [3, 3, 1]
    bars2 = [4, 2, 3]
    bars3 = [4, 6, 7, 10, 4, 4]
    bars4 = bars1 + bars2 + bars3
    
    # The X position of bars
    r1 = [1,5,9]
    r2 = [2,6,10]
    r3 = [3,4,7,8,11,12]
    r4 = r1 + r2 + r3
    
    # # Create barplot
    # plt.bar(r1, bars1, width = barWidth, color = (0.3,0.1,0.4,0.6), label='Alone')
    # plt.bar(r2, bars2, width = barWidth, color = (0.3,0.5,0.4,0.6), label='With Himself')
    # plt.bar(r3, bars3, width = barWidth, color = (0.3,0.9,0.4,0.6), label='With other genotype')

    plt.bar(r1, bars1, width = barWidth, color = (0.55, 0, 0.0, 1), label='Alone')
    plt.bar(r2, bars2, width = barWidth, color = (0, 0.39, 0, 1), label='With Himself')
    plt.bar(r3, bars3, width = barWidth, color = (0.3,0.9,0.4, 1), label='With other genotype')
    # Note: the barplot could be created easily. See the barplot section for other examples.
    
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
    plt.savefig('./Prototype/backend/Algorithm/examples/barplot_dpi200.png', dpi=200)
    plt.show()

def generateRefBarPlot_2Groups():
    # Sample data
    categories = ['A', 'B', 'C', 'D', 'E']
    values_group1 = [10, 23, 15, 30, 18]
    values_group2 = [12, 18, 20, 25, 22]

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
    # generateRefBarPlot()
    generateRefBarPlot_2Groups()
    # generateRefPieChart()