from PyPDF2 import PdfFileMerger
import os

merger_path = os.path.dirname(os.path.abspath(__file__))
pdfs_path = os.path.abspath("{}{}".format(merger_path, '/input'))
files = os.listdir(pdfs_path)
merger = PdfFileMerger()
free_pos = [str(i) for i in range(len(files)-1)]
pos = free_pos[:]
for pdf in files:
    file_extension = os.path.splitext(os.path.basename(pdf))[1]
    if file_extension == '.pdf':
        pdf_pos = input("{} {} {} {} {}".format("Enter one of the free positions", free_pos, "for", pdf, ': '))
        while not pdf_pos in free_pos:
            pdf_pos = input("{} {} {} {} {}".format("This was not valid value. Please enter one of the free positions", free_pos, "for", pdf, ': '))
        free_pos.remove(pdf_pos)
        pos[int(pdf_pos)] = pdf
for pdf in pos:
    pdf_path = os.path.abspath("{}{}{}".format(pdfs_path, '/', pdf))
    merger.append(open(pdf_path, 'rb'))
output = os.path.abspath("{}{}".format(merger_path, "/output"))
if not os.path.exists(output):
    os.makedirs(output)
pdf_name = input("{}".format("Enter the name of the result PDF file: "))
output_file = os.path.abspath("{}{}{}{}".format(output, '/', pdf_name, '.pdf'))
merger.write(output_file)
