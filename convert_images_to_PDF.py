import img2pdf
import os

folder = "" # Input the folder that contains all the images you need to add to a particular pdf.

# Full paths of images
images = [os.path.join(folder, f) for f in os.listdir(folder)]
images.sort()  # ensures proper order

preferred_name_of_pdf = " " # Enter your preferred name for the PDF
# Convert to PDF
with open(f"{preferred_name_of_pdf}.pdf", "wb") as f:
    f.write(img2pdf.convert(images))

print("PDF created successfully!")
