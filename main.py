from PIL import Image
from roipoly import RoiPoly

import numpy as np
import matplotlib.pyplot as plt

# Read source image :
source = np.array(Image.open('Pictures/orca.jpg'))
nb_row_s,nb_col_s,nb_ch_s = source.shape

plt.figure()
plt.imshow(source)
plt.axis('off')

# Select and display polygon in source picture
poly = RoiPoly(color='r')
x_poly = np.around(poly.x) 
y_poly = np.around(poly.y) 

# Bounding rectangle of poly
y_min = min(y_poly)
y_max = max(y_poly)
x_min = min(x_poly)
x_max = max(x_poly)

# Read target image :
target = np.array(Image.open('Pictures/mountains.jpg'))
nb_row_t,nb_col_t,nb_ch_t = target.shape

plt.figure()
plt.imshow(target)
plt.axis('off')

# Select rectangle in target
print('Select opposite corners of the target zone');
[p1,p2] = plt.ginput(2);
x_min_r = max(min(p1[0], p2[0]), 0)
x_max_r = min(max(p1[0], p2[0]), nb_col_t)
y_min_r = max(min(p1[1], p2[1]), 0)
y_max_r = min(max(p1[1], p2[1]), nb_row_t)

plt.plot([x_min_r, x_min_r], [y_min_r, y_max_r], color='red')
plt.plot([x_min_r, x_max_r], [y_min_r, y_min_r], color='red')
plt.plot([x_max_r, x_max_r], [y_min_r, y_max_r], color='red')
plt.plot([x_min_r, x_max_r], [y_max_r, y_max_r], color='red')
plt.show()
