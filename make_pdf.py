import os
from bs4 import BeautifulSoup
import re
from pypdf import PdfWriter
from PIL import Image  # install by > python3 -m pip install --upgrade Pillow  # ref. https://pillow.readthedocs.io/en/latest/installation.html#basic-installation
from pillow_heif import register_heif_opener

register_heif_opener()

def is_image(filepath):
    return filepath.endswith(".jpeg") or \
        filepath.endswith(".jpg") or \
        filepath.endswith(".png")

def get_name(filepath):
    headdir = os.path.split(filepath)[0]
    subdir = os.path.split(filepath)[1]
    if re.match("^\.\/[^/]*$", headdir):
        name, other = re.split(" - ", subdir)
        return name
    else:
        return get_name(headdir)
    
text = []
pdfs = []
image_paths = []

for subdir, dirs, files in os.walk("."):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file

        if filepath.endswith(".html"):
            with open(filepath) as f:
                s = f.read()
                c = BeautifulSoup(s).text
                name = get_name(filepath)
                text.append(f"{name}: {c}")
        elif filepath.endswith(".pdf"):
            pdfs.append(filepath)
        elif is_image(filepath):
            image_paths.append(filepath)

def output_text():
    print("\n".join(text))

def output_pdfs():
    merger = PdfWriter()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("result.pdf")
    merger.close()

def output_images():
    images = [
        Image.open(f)
        for f in image_paths
    ]

    pdf_path = "tmp.pdf"
        
    images[0].save(
        pdf_path, "PDF" ,resolution=400.0, save_all=True, append_images=images[1:]
    )
    pdfs.append(pdf_path)

output_images()
output_text()
output_pdfs()