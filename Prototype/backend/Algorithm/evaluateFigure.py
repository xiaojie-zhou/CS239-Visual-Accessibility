import cv2
import numpy as np
from sklearn.cluster import DBSCAN
from scipy.spatial.distance import euclidean
import os

def evaluateFigure(input_path, color_palette='normal'):
    return np.random.randint(60, 100)

if __name__ == '__main__':
    score = evaluateFigure(input_path='/Prototype/backend/Algorithm/barplot_raw.png',
                    color_palette='normal')
    print(score)