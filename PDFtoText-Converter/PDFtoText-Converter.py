import PyPDF2
import wordninja

# Open the PDF file
pdf_file = open('document.pdf', 'rb')

# Create a PDF file reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Create a variable to hold the entire text
text = ''
# Loop through each page and extract the text
for page in range(num_pages):
    page_obj = pdf_reader.pages[page]
    page_text = page_obj.extract_text()
    words = wordninja.split(page_text)
    for w in words:
        text += w + ' '
    text += '\n\n'

# Save the text to a file
with open('example.txt', 'w') as file:
    file.write(text)

# Close the PDF file
pdf_file.close()

# Print a message to indicate the conversion is complete
print("PDF to text conversion complete!")