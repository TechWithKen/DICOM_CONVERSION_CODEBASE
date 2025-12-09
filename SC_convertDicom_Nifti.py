import pydicom
import os
import subprocess

downloaded_dicom_file = " "  # Add the path to the folder containing the DICOM files.

try:
    dicom_images = os.listdir(downloaded_dicom_file)

    def convert_to_nifti(medical_images):


        for d_file in medical_images:
            ds = pydicom.dcmread(f'{downloaded_dicom_file}/{d_file}')

            def detect_sequence(dicom_file):


                dicom = pydicom.dcmread(f'{downloaded_dicom_file}/{dicom_file}')
                series_desc = getattr(dicom, "SeriesDescription", "").lower()
                protocol_name = getattr(dicom, "ProtocolName", "").lower()
                text = series_desc + " " + protocol_name

                if "t1" in text:
                    return "T1"

                elif "t2" in text:
                    return "T2"

                elif "flair" in text:
                    return "FLAIR"

                elif "dwi" in text:
                    return "DWI"

                else:
                    return "UNKNOWN"

            series_to_seq = {}
            patient_name = ds.PatientName
            series_uid = ds.SeriesInstanceUID

            if series_uid not in series_to_seq:
                seq_type = detect_sequence(d_file)
                series_to_seq[series_uid] = seq_type

            input_folder = downloaded_dicom_file
            output_folder = downloaded_dicom_file

            for series_uid, seq_type in series_to_seq.items():
                subprocess.call([
                "dcm2niix",
                "-o", output_folder,           # output folder
                "-b", "n",                     # don't create JSON
                "-f", f"{patient_name}_{seq_type}",     # filename template: protocol + sequence + series number
                input_folder
            ])

        return "Created Nifti Files Successfully."

    print(convert_to_nifti(dicom_images))

except FileNotFoundError:
    print("NO FILE FOUND: The file that you need isn't present, please check that the file path is correct added.")

except NotADirectoryError:
    print("NO FOLDER ADDED: The path to the file you have entered is not a valid folder path, please make sure/"
          "you enter the correct directory.")