import os
import pydicom
import dicom2nifti as dcm2niix
import nibabel as nib

def get_patient_id_and_image_type(dicom_file):
    try:
        ds = pydicom.dcmread(dicom_file)
        patient_id = getattr(ds, "PatientID", "Unknown")
        image_type = "_".join(getattr(ds, "ImageType", ["Unknown"]))
        return patient_id, image_type
    except Exception as e:
        print(f"Error reading DICOM file: {dicom_file}. Error: {e}")
        return "Unknown", "Unknown"


def has_sufficient_slices(dicom_directory):

    slice_count = 0
    for file in os.listdir(dicom_directory):
        if file.lower().endswith(".dcm"):
            slice_count += 1
    return slice_count >= 3   # threshold


def rename_files_with_patient_id(output_subdir, patient_id):
    for generated_file in os.listdir(output_subdir):
        if generated_file.endswith(".nii.gz") or generated_file.endswith(".nii"):
            original_name, ext = os.path.splitext(generated_file)

            if ext == ".gz":
                original_name, extra_ext = os.path.splitext(original_name)
                ext = extra_ext + ext

            new_filename = f"{patient_id}_{original_name}{ext}"
            os.rename(
                os.path.join(output_subdir, generated_file),
                os.path.join(output_subdir, new_filename)
            )
            print(f"Renamed: {generated_file} -> {new_filename}")


def convert_dicom_to_nifti(input_directory, output_directory):
    for root, _, files in os.walk(input_directory):
        first_dicom = None

        for file in files:
            if file.lower().endswith(".dcm"):
                first_dicom = os.path.join(root, file)
                break

        if not first_dicom:
            continue

        if not has_sufficient_slices(root):
        	print(f"Skipping {root}: Insufficient slices for NIFTI conversion.")
        	continue

        try:
            patient_id, image_type = get_patient_id_and_image_type(first_dicom)
            subfolder_name = f"{patient_id}_{image_type}"
            output_subdir = os.path.join(output_directory, subfolder_name)

            os.makedirs(output_subdir, exist_ok=True)

            # Convert directory using dcm2niix (expected but missing)
            dcm2niix.convert_directory(root, output_subdir)

            rename_files_with_patient_id(output_subdir, patient_id)

        except Exception as e:
            print(f"Failed to convert {root}. Error: {e}")


# Paths
input_directory = "C:/Users/ti664/DATICAN/SORTED/MR/NECK/UDCS/YAB/18"
output_directory = "C:/Users/ti664/DATICAN/SORTED/MR/NECK/UDCS/YAB/18"

convert_dicom_to_nifti(input_directory, output_directory)


