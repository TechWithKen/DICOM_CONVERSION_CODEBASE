import img2pdf
import os

folder = "C:/Users/ti664/OneDrive/Desktop/images"

# Full paths of images
images = [os.path.join(folder, f) for f in os.listdir(folder)]
images.sort()  # ensures proper order

# Convert to PDF
with open("NewConvertedFiles.pdf", "wb") as f:
    f.write(img2pdf.convert(images))

print("PDF created successfully!")
