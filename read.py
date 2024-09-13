

import PyPDF2
import re

def is_date_format(text):
    # Define the regular expression pattern for the date format DD/MM/YYYY
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    
    # Use re.match to check if the text matches the pattern
    if re.match(pattern, text):
        return True
    else:
        return False
    
def contains_page_info(text):
    # Define the regular expression pattern for "Page X of Y"
    pattern = r'^Page \d+ of 12028'
    
    # Use re.match to check if the text matches the pattern
    if re.match(pattern, text):
        return True
    else:
        return False

def extract_text_from_pdf(pdf_path):
	# Open the PDF file in read-binary mode
	with open(pdf_path, 'rb') as file:
		# Create a PDF reader object
		reader = PyPDF2.PdfReader(file)
		
		# Initialize a string to store the extracted text
		extracted_text = ""
		
		# Loop through each page of the PDF
		for page_num in range(len(reader.pages)):
			# Extract text from each page
			page = reader.pages[page_num]
			extracted_text += page.extract_text()
		
	# Return the extracted text
	return extracted_text.split('\n')[7:]

def process_page(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    data = ''
    for line in text:
        if is_date_format(line):
            data += '\n'
        if contains_page_info(line):
            break
        data += line + ' '

    lines = data.split('\n')
    for line in lines:
        print(line.strip())

# Example usage
pdf_path = 'page/page_550.pdf'
process_page(pdf_path)