from PIL import Image
from roipoly import RoiPoly

import numpy as np
import matplotlib.pyplot as plt


# Read source image :
source = np.array(Image.open('Pictures/orca.jpg'))
nb_row_s,nb_col_s,nb_ch_s = source.shape

plt.imshow(source)
plt.axis('off')

# Select and display polygon in source picture
# Axes : x to the right, y to the top !
poly = RoiPoly(color='r')
x_poly = np.around(poly.x) 
y_poly = np.around(poly.y) 

# Bounding rectangle of poly
y_min = min(y_poly)
y_max = max(y_poly)
x_min = min(x_poly)
x_max = max(x_poly)
