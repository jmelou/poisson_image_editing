from PIL import Image
from roipoly import RoiPoly

import numpy as np
import matplotlib.pyplot as plt

from skimage.transform import rescale, resize

# Read source image :
source = np.array(Image.open('Pictures/orca.jpg'))
nb_row_s,nb_col_s,nb_ch_s = source.shape

s = plt.figure()
plt.imshow(source)
plt.axis('off')

# Select and display polygon in source picture
poly = RoiPoly(color='r')
source_1c = source[:,:,0]
polygonMask = poly.get_mask(source_1c)

x_poly = np.around(poly.x) 
y_poly = np.around(poly.y) 

# Bounding rectangle of poly
i_p_min = int(min(y_poly))
i_p_max = int(max(y_poly))
j_p_min = int(min(x_poly))
j_p_max = int(max(x_poly))

# Read target image :
target = np.array(Image.open('Pictures/mountains.jpg'))
nb_row_t,nb_col_t,nb_ch_t = target.shape

t = plt.figure()
plt.imshow(target)
plt.axis('off')

# Select rectangle r in target
print('Select opposite corners of the target zone');
[p1,p2] = plt.ginput(2);
j_r_min = int(max(min(p1[0], p2[0]), 0))
j_r_max = int(min(max(p1[0], p2[0]), nb_col_t))
i_r_min = int(max(min(p1[1], p2[1]), 0))
i_r_max = int(min(max(p1[1], p2[1]), nb_row_t))

plt.plot([j_r_min, j_r_min], [i_r_min, i_r_max], color='red')
plt.plot([j_r_min, j_r_max], [i_r_min, i_r_min], color='red')
plt.plot([j_r_max, j_r_max], [i_r_min, i_r_max], color='red')
plt.plot([j_r_min, j_r_max], [i_r_max, i_r_max], color='red')
plt.draw()

# Target sub-matrix corresponding to the rectangle r :
r = target[i_r_min:i_r_max,j_r_min:j_r_max,:]

# Select the sub-matrices in the bounding box of the polygon :
source = source[i_p_min:i_p_max,j_p_min:j_p_max,:];
polygonMask = polygonMask[i_p_min:i_p_max,j_p_min:j_p_max];

# Resize s and p :
nb_row_r,nb_col_r,nb_ch_r = r.shape
source = resize(source, r.shape, anti_aliasing=True, mode='constant')
polygonMask = resize(polygonMask, r.shape, anti_aliasing=True, mode='constant')

plt.show()
