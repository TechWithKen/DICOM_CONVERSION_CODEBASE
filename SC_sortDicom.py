import os
import shutil
import pydicom


downloaded_data_path = "" # import the path in string to the containing portion of the dataset.

dicom_images = os.listdir(downloaded_data_path)

def sort_dicom_images(medical_images):


	for dm_images in medical_images:

		ds = pydicom.dcmread(f'{downloaded_data_path}/{dm_images}')
		modality = ds.Modality
		body_part_examined = ds.BodyPartExamined
		patient_id = ds.PatientID.replace("..", "")
		if body_part_examined == "????":
			body_part_examined = "missingBodyPart"
		

		pathway_med_images = f'{modality}/{body_part_examined}/{patient_id}'

		os.makedirs(pathway_med_images, exist_ok = True)   

		source_file = f'{downloaded_data_path}/{dm_images}'
		destination_folder = pathway_med_images
		shutil.copy(source_file, destination_folder)


	return "Sorted! please check your folder."


print(sort_dicom_images(dicom_images))