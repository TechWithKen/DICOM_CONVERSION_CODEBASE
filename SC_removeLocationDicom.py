import numpy as np
import pydicom

ds = pydicom.dcmread("C:/Users/ti664/DATICAN/UnnAnnonymized_Dataset/Annoymized/002.dcm")
px = ds.pixel_array.copy()

print(px.shape)

# Example wiping out top 50 rows of pixels
"""px[:50, :] = 0

ds.PixelData = px.tobytes()
ds.save_as("pixel_cleaned.dcm")"""


import matplotlib.pyplot as plt

img = "C:/Users/ti664/DATICAN/UnnAnnonymized_Dataset/Annoymized/002.dcm"

plt.imshow(img, cmap='gray')
plt.show()
