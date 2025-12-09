"""Documentation:
This Source code is used to sort Digital Image Communication in Medicine (DICOM) files
based on the way they are named. This sorting source code uses 1 external and 2 built-in
libraries. To install them, simply use 'pip install libraryname'. """


import os
import shutil
import pydicom

downloaded_data_path = " "# import the path in string of the folder containing the dataset.

try:
    dicom_images = os.listdir(downloaded_data_path)

    def sort_dicom_images(medical_images):
        """Working on the principle of Metadata providing more information on the content of the DICOM file,
        A sorting function was built to read the metadata and use them as the name of the subfolders leading up to the file
        stored."""


        for dm_images in medical_images:

            if dm_images[-3:] == "dcm": # ensuring that only dicom files are checked and sorted. to avoid errors.
                ds = pydicom.dcmread(f'{downloaded_data_path}/{dm_images}')
                modality = ds.Modality
                body_part_examined = ds.BodyPartExamined
                patient_id = ds.PatientID.replace("..", "")# some patientID has the identifier .. at the end.

                if body_part_examined == "????":
                    body_part_examined = "missingBodyPart"
                else:
                    pathway_med_images = f'{modality}/{body_part_examined}/{patient_id}'
                    os.makedirs(pathway_med_images, exist_ok = True)  # create a folder but check first if it exists
                    source_file = f'{downloaded_data_path}/{dm_images}'
                    destination_folder = pathway_med_images
                    shutil.copy(source_file, destination_folder) # transfer the main DICOM file itself to the new location
            else:
                pass

        return "Sorted! please check your folder."

    if __name__ == "__main__":
        print(sort_dicom_images(dicom_images))

except FileNotFoundError:
    print("NO FILE FOUND: The file that you need isn't present, please check that the file path is correct added.")

except NotADirectoryError:
    print("NO FOLDER ADDED: The path to the file you have entered is not a valid folder path, please make sure/"
          "you enter the correct directory.")