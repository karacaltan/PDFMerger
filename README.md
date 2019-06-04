# PDFMerger

This is a simple script for merging multiple PDF files into a single PDF file. You can manually set the position for each PDF file.
It is also possible to define a custom PDF file name of the result file. The result PDF file can be find in the directory `output`.

### Requirements
Python 3.7.x

### Try it out
Create a directory called `input` and place your PDF files in it.

It is recommended to install a virtual environment. Create and activate the virtual environment

    python -m venv env
    source env/bin/activate

Install dependencies

    python -m pip install -r requirements.txt

Run `pdf_merger.py`	
	
### Reset
Deactivate and remove the virtual environment

    deactivate
    rm -rf env
