import pydicom
import os


downloaded_data_path = "C:/Users/ti664/DATICAN/SORTED/dicomimages"
dicom_images = os.listdir(downloaded_data_path)

path = f"{downloaded_data_path}/Annoymized"
os.makedirs(path, exist_ok = True)

for userid, d_images in enumerate(dicom_images):
	if d_images[-3:] == "dcm":
		ds = pydicom.dcmread(f'{downloaded_data_path}/{d_images}')
		modality = ds.Modality
		body_part = ds.get("BodyPartExamined", "NONE")
		patient_id = ds.PatientID 
		acquisition_date = ds.AcquisitionDate
		if "InstitutionName" in ds:
			del ds.InstitutionName
		ds.PatientName = f'{modality}_{body_part}_{acquisition_date}_{userid:03d}'

		output_path = f"{path}/{userid:03d}.dcm"
		print(f"{userid:03d} done")
		ds.save_as(output_path)

	else:
		pass
