"""
sortdicom.py

This script sorts DICOM (.dcm) files into organized folders based on their
metadata, including Modality, BodyPartExamined, and PatientID.

The sorted structure looks like:

    Modality /
        BodyPartExamined /
            PatientID /
                file.dcm

Requirements:
    - pydicom
    - shutil (built-in)
    - os (built-in)

Usage:
    1. Set the path to your folder of DICOM files.
    2. Run the script.
"""

import os
import shutil
import pydicom


def read_dicom_metadata(file_path):
    """Safely read metadata from a DICOM file.

    Returns:
        tuple: (modality, body_part, patient_id)
    """
    ds = pydicom.dcmread(file_path)

    modality = getattr(ds, "Modality", "UNKNOWN")
    patient_id = getattr(ds, "PatientID", "NO_ID")
    body_part = getattr(ds, "BodyPartExamined", "UNKNOWN")

    if body_part == "????":
        body_part = "UNKNOWN"

    # Clean patient ID
    patient_id = patient_id.replace("..", "")

    return modality, body_part, patient_id


def generate_output_path(modality, body_part, patient_id):
    """Create an output directory path based on metadata."""
    return os.path.join(modality, body_part, patient_id)


def sort_dicom_images(input_folder):
    """Sort all DICOM files inside a folder into structured subdirectories."""

    dicom_files = os.listdir(input_folder)

    for dicom_file in dicom_files:
        if not dicom_file.lower().endswith(".dcm"):
            continue  # skip non-dicom files

        file_path = os.path.join(input_folder, dicom_file)
        print(file_path)

        modality, body_part, patient_id = read_dicom_metadata(file_path)

        output_path = generate_output_path(modality, body_part, patient_id)
        os.makedirs(output_path, exist_ok=True)

        shutil.copy(file_path, output_path)

    return "Sorting complete. Check your output folders."


if __name__ == "__main__":
    downloaded_data_path = " "  # <-- PUT YOUR PATH HERE

    try:
        print(sort_dicom_images(downloaded_data_path))

    except FileNotFoundError:
        print("ERROR: The folder was not found. Check your path and try again.")

    except NotADirectoryError:
        print("ERROR: The path you entered is not a valid directory.")
