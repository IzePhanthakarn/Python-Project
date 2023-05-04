import PyPDF2

# Function to split PDF document
def split_pdf(input_path, output_path, pages):
    pdf_reader = PyPDF2.PdfReader(input_path)
    pdf_writer = PyPDF2.PdfWriter()
    for page in pages:
        pdf_writer.add_page(pdf_reader.pages[page])
    with open(output_path, 'wb') as f:
        pdf_writer.write(f)

# Split a PDF document with pages 2 to 4
input_path = 'document.pdf'
output_path = 'split_document.pdf'
pages = [0, 9] # 0-based index
split_pdf(input_path, output_path, pages)