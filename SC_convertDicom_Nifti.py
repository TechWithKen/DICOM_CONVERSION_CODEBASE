import pydicom
import os
import subprocess

downloaded_dicom_file = " "  # Add the path to the folder containing the DICOM files.

try:
    dicom_images = os.listdir(downloaded_dicom_file)

    def convert_to_nifti(medical_images):
        """NIFTI files are majorly used for MRI scans as they are gotten from the BRAIN.
        since NIFTI is connected to Neuroimaging it's important to convert it to 3D. A NIFTI file is gotten from the
        combination of multiple DICOM file (known as slices) combined and collated in a unique way that they form
        together to form one bunch huge bunch of NIFTI file. This function is used to convert multiple slices of DICOM
        files into one single unit of NIFTI file. However it also states the sequence it represents. T1 weighted and co.
         """


        for d_file in medical_images:
            ds = pydicom.dcmread(f'{downloaded_dicom_file}/{d_file}')

            def detect_sequence(dicom_file):
                """Useful to detect the sequence of the given dicom file, based of the protocol name and series
                description. Sometimes it's from series name, other times it's from protocol name. Since there is
                no one size fit all, both of them are concatenated to form a string, and then it's checked."""


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

            if series_uid not in series_to_seq:  # Collate seriesID of DICOM files that are similar into one key
                seq_type = detect_sequence(d_file)
                series_to_seq[series_uid] = seq_type

            input_folder = downloaded_dicom_file
            output_folder = downloaded_dicom_file

            for series_uid, seq_type in series_to_seq.items():
                subprocess.call([
                "dcm2niix",
                "-o", output_folder,           # output folder
                "-b", "n",                     # don't create JSON
                "-f", f"{patient_name}_{seq_type}",     # filename template: anonymized(patient name) + sequence weight
                input_folder
            ])

        return "Created Nifti Files Successfully."

    if __name__ == "__main__":
        print(convert_to_nifti(dicom_images))

except FileNotFoundError:
    print("NO FILE FOUND: The file that you need isn't present, please check that the file path is correct added.")

except NotADirectoryError:
    print("NO FOLDER ADDED: The path to the file you have entered is not a valid folder path, please make sure/"
          "you enter the correct directory.")