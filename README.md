DICOM CONVERSION CODEBASE
A simple, clean, and powerful set of Python tools for working with medical imaging files.
About This Project
DICOM CONVERSION CODEBASE is a collection of Python scripts created to help beginners and developers work with DICOM files  the special type of files used in hospitals to store medical scans like MRI, CT, and X-ray images.
This project started from my personal obsession with cancer research, medical imaging, and understanding how computers can study images through code and make smart decisions from them.
It is built for:
 Python developers


 Beginners in Machine Learning


 Anyone curious about how medical images are processed using code


What This Codebase Can Do
This repository contains multiple Python scripts that perform real medical imaging tasks, such as:
🔹 1. Anonymizing DICOM Files
Some DICOM files contain sensitive information like:
Patient Name


Patient Location


Patient ID


The code de-identifies the DICOM file by removing these details so the file becomes safe to use for research and model development.
🔹 2. Sorting DICOM Files Automatically
DICOM files often come in huge, scattered datasets.
 One script organizes them into clean folders based on metadata such as:
Patient name


Patient ID


Study or series information
This makes the dataset neat and easy to work with.
🔹 3. Converting DICOM Slices into NIfTI
Some medical scans are made up of many DICOM slices.
 Another script:
Collects these slices


Organizes them


Converts them into a single NIfTI file, a format used a lot in machine learning and brain-imaging research.


🔸 Note:
 NIfTI conversion requires an Anaconda environment, because the script uses a subprocess call to dicom2nifti inside Conda.
Technologies Used
This project is written entirely in Python, using:
pydicom — to read and edit DICOM files


shutil — for copying and file operation


os — for directory handling


dicom2nifti — for converting DICOM slices to NIfTI



Basic requirements:
Python (any modern version)


Anaconda (for NIfTI conversion script)


DICOM files (real patient data is not included)


Dataset Information
This project uses over 2,000 DICOM files inside DATICAN (Research lab).
 Some of them are de-identified, some are not.
 None of these files are uploaded to GitHub.
But the code is portable — meaning:
You can use this code with any publicly available DICOM dataset.
How to Use This Codebase
Clone the repository

 git clone https://github.com/yourusername/DICOM-CONVERSION-CODEBASE.git
Open the folder in your preferred Python editor


Run any script you want
 For example:


Anonymizer


Sorter


DICOM → NIfTI converter


No special command-line instructions needed : the code uses basic Python functions.
Exception:
 NIfTI conversion script must be run from an Anaconda environment.
Project Status
This project is still under development.
 Planned improvements include:
Using NumPy to edit or remove location metadata directly from pixel arrays


Understanding DICOM sequences automatically without manually specifying tags


Adding a complete Standard Operating Procedure (SOP)


Adding full, detailed documentation for each script


Right now, the code works well and is clean, but more features will be added.
Author
Kehinde Ajasa
 Research Intern — DATICAN
 Passionate about medical imaging, machine learning, and cancer research.
Why This Project Matters
Medical imaging is one of the most powerful tools in understanding the human body.
 With the right code, computers can help doctors:
Detect tumors


Study cancer growth


Analyze brain scans


Understand patterns humans may miss


This repository is a small step toward that dream — and it is built so that even beginners can start learning.
