"""
dicom_anonymizer.py

This module anonymizes DICOM (Digital Imaging and Communications in Medicine)
files by removing or modifying patient-identifiable metadata.


The anonymization process works as follows:
1. Each DICOM file is read.
2. Metadata fields containing patient information are accessed.
3. Identifiable fields are cleared or replaced.
4. The modified DICOM file is saved as a new file, leaving the original intact.

This module can process:
- A single DICOM file.
- A folder containing multiple DICOM files (recursively).

Notes:
- The module relies on the `pydicom` library.
- Metadata is mutable, so new DICOM files are created instead of modifying
  the originals.
- The module is designed for ethical research and educational purposes only.
"""

import pydicom
import os

def read_dicom_metadata(file_path):
    """
    :param file_path:
    :return: tuple of three items (modality, body_part, acquisition_date
    """

    ds = pydicom.dcmread(file_path)
    modality = getattr(ds, "Modality", "NONE")
    body_part = getattr(ds,"BodyPartExamined", "NONE")
    acquisition_date = getattr(ds, "AcquisitionDate", "NONE")

    return modality, body_part, acquisition_date


def create_output_path(user_folder):
    """
    :param user_folder:
    :return:
    """
    created_folder = "Anonymized"

    return os.path.join(user_folder, created_folder)


def anonymize_patient_name(user_folder):
    """
    :param user_folder:
    :return:
    """

    dicom_images = os.listdir(user_folder)
    for dicom_image in dicom_images:
        file_path = os.path.join(user_folder, dicom_image)
        modality, body_part, acquisition_date = read_dicom_metadata(file_path)

        if not dicom_image.lower().endswith(".dcm"):
            continue
        ds = pydicom.dcmread(dicom_images)
        ds.patient_name = f'{modality}_{body_part}_{acquisition_date}'

    return ds.PatientName


def del_location_in_dicom(user_folder):
    """
    :param user_folder:
    :return:
    """

    dicom_images = os.listdir(user_folder)
    for dicom_image in dicom_images:
        file_path = os.path.join(user_folder, dicom_image)

        if dicom_images[-3:] == "dcm":
            ds = pydicom.dcmread(file_path)

            if "InstitutionName" in ds:
                del ds.InstitutionName

    return None


def copy_anonymized(user_folder):
    """

    :param user_folder
    :return:
    """

    dicom_images = os.listdir(user_folder)

    for index, dicom_image in enumerate(dicom_images):
        if not dicom_image.lower().endswith(".dcm"):
            continue

        folder_location = "Anonymized"
        file_id = f'{index}.dcm'
        storage_path = os.path.join(user_folder, folder_location, file_id)

    return storage_path