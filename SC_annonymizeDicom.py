"""Documentation:
This Source code is used to Anonymize Digital Image Communication in Medicine (DICOM) files
gotten from hospitals and Medical Laboratories. The idea is that when DICOM files are created by the Radiologist
it stores personal information of the patient as METADATA used to describe the existence of the dicom files,
and it's illegal and unethical to use these dicom files without de-identification. This Source code is will be used
to anonymize any given dicom file or folders containing a dicom file"""


import pydicom
import os

downloaded_data_path = " "  # Add the path to the folder containing the Raw DICOM files.


try:
    path = f"{downloaded_data_path}/Anonymized"  # Creating a new path from the original path, to store the anonymized DICOM files.
    os.makedirs(path, exist_ok = True)

    dicom_images = os.listdir(downloaded_data_path)


    def anon_dicom_images(medical_images):
        """DICOM images stores its data in a 'Metadata' field, and it's mutable. Hence, Each DICOM file will be read,
         the Metadata stored will be accessed, and it will be changed and then re-saved as a new DICOM image.
         So we are basically creating new DICOM images but with a changed Metadata since it has been changed due to the
         mutability of the previous metadata containing DICOM file."""

        for userid, d_images in enumerate(medical_images):

            if d_images[-3:] == "dcm":
                ds = pydicom.dcmread(f'{downloaded_data_path}/{d_images}')
                modality = ds.Modality
                body_part = ds.get("BodyPartExamined", "NONE")
                acquisition_date = ds.AcquisitionDate

                if "InstitutionName" in ds:
                    del ds.InstitutionName

                ds.PatientName = f'{modality}_{body_part}_{acquisition_date}_{userid:03d}'
                output_path = f"{path}/{userid:03d}.dcm"
                print(f"{userid:03d} done")  # Status checker to show when each dicom file is created.
                ds.save_as(output_path)

            else:
                pass
        return "All Dicom files present in folder has been anonymized successfully."

    if __name__ == "__main__":
        print(anon_dicom_images(dicom_images))

except FileNotFoundError:
    print("NO FILE FOUND: The file that you need isn't present, please check that the file path is correct added.")

except NotADirectoryError:
    print("NO FOLDER ADDED: The path to the file you have entered is not a valid folder path, please make sure/"
          "you enter the correct directory.")