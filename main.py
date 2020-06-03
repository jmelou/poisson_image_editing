from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Read source image :
source = np.array(Image.open('Pictures/orca.jpg'))
nb_row_s,nb_col_s,nb_ch_s = source.shape

plt.imshow(s)
plt.show()
