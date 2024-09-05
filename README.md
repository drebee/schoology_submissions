# install dependencies

Assuming you have conda set up on your computer:

```
conda install pypdf
conda install Pillow
pip install --upgrade pip setuptools wheel
pip install pillow-heif
```

# usage

1. In schoology, go to the page for the assisgnment and click the little icon to download.
2. Unzip
3. Drag the unzipped folder to this directory
4. Navigate to this directory in a terminal (activate conda if needed) and run `python make_pdf.py`