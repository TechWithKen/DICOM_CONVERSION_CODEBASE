"""
dicom_anonymizer.py

This module anonymizes DICOM files by removing or modifying
patient-identifiable metadata.

It can process:
- A single DICOM file
- A folder containing multiple DICOM files

Notes:
- Uses the pydicom library
- Original files are never overwritten
"""

import pydicom
import os
import shutil


def read_dicom_metadata(file_path):
    """
    :param file_path:
    :return: tuple (modality, body_part, acquisition_date)
    """
    ds = pydicom.dcmread(file_path)
    modality = getattr(ds, "Modality", "NONE")
    body_part = getattr(ds, "BodyPartExamined", "NONE")
    acquisition_date = getattr(ds, "AcquisitionDate", "NONE")
    return modality, body_part, acquisition_date


def create_output_path(user_folder):
    """
    Creates 'Anonymized' folder inside the user directory
    """
    created_folder = os.path.join(user_folder, "Anonymized")

    if not os.path.exists(created_folder):
        os.makedirs(created_folder)

    return created_folder


def anonymize_patient_name(user_folder):
    """
    Replaces patient name with safe auto-generated metadata
    """
    dicom_images = os.listdir(user_folder)

    for dicom_image in dicom_images:
        file_path = os.path.join(user_folder, dicom_image)

        if not dicom_image.lower().endswith(".dcm"):
            continue

        modality, body_part, acquisition_date = read_dicom_metadata(file_path)
        ds = pydicom.dcmread(file_path)

        # Safe replacement for PatientName
        safe_name = f"{modality}_{body_part}_{acquisition_date}"
        ds.PatientName = safe_name

        # Save into anonymized output folder
        output_path = create_output_path(user_folder)
        save_path = os.path.join(output_path, dicom_image)
        ds.save_as(save_path)

    return "PatientName anonymization complete."


def del_location_in_dicom(user_folder):
    """
    Removes InstitutionName field if present
    """
    output_folder = create_output_path(user_folder)
    dicom_images = os.listdir(output_folder)

    for dicom_image in dicom_images:
        file_path = os.path.join(output_folder, dicom_image)

        if not dicom_image.lower().endswith(".dcm"):
            continue

        ds = pydicom.dcmread(file_path)

        if hasattr(ds, "InstitutionName"):
            del ds.InstitutionName

        ds.save_as(file_path)

    return "InstitutionName removed from anonymized files."


def copy_anonymized(user_folder):
    """
    Ensures anonymized files are copied with numeric IDs
    """
    output_folder = create_output_path(user_folder)
    dicom_images = [
        f for f in os.listdir(output_folder)
        if f.lower().endswith(".dcm")
    ]

    final_folder = os.path.join(user_folder, "Anonymized_Final")
    os.makedirs(final_folder, exist_ok=True)

    for index, dicom_image in enumerate(dicom_images):
        src = os.path.join(output_folder, dicom_image)
        dst = os.path.join(final_folder, f"{index}.dcm")
        shutil.copy(src, dst)

    return "Final anonymized numeric copies saved."


if __name__ == "__main__":
    downloaded_data_path = " "

    if downloaded_data_path == "":
        print("Error: Please set downloaded_data_path to your DICOM folder.")
    else:
        print(anonymize_patient_name(downloaded_data_path))
        print(del_location_in_dicom(downloaded_data_path ))
        print(copy_anonymized(downloaded_data_path))
        print("Anonymization Pipeline Completed Successfully.")
