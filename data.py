import zipfile

# Path to the zip file
file_path = r"C:\Users\Kusha\OneDrive\Desktop\EndToEnd\Fanformers\archive (2).zip"

extract_path = r"C:\Users\Kusha\OneDrive\Desktop\EndToEnd\Fanformers\Dataset"

with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
