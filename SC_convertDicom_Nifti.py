import pydicom
import os
import subprocess

downloaded_dicom_file = "C:/Users/ti664/DATICAN/SORTED/CR/BREAST/MAMMO/2020/407"


dicom_path = os.listdir(downloaded_dicom_file)

for d_file in dicom_path:
    def detect_sequence(dicom_file):
        ds = pydicom.dcmread(f'{downloaded_dicom_file}/{dicom_file}')
        series_desc = getattr(ds, "SeriesDescription", "").lower()
        protocol_name = getattr(ds, "ProtocolName", "").lower() 
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
    ds = pydicom.dcmread(f'{downloaded_dicom_file}/{d_file}')
    modality = ds.Modality
    patient_name = ds.PatientName
    series_uid = ds.SeriesInstanceUID
    print(series_uid)
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
        "-f", f"{modality}_{seq_type}",     # filename template: protocol + sequence + series number
        input_folder
    ])



