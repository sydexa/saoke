
import PyPDF2

def split_pdf(input_pdf_path, output_folder):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_pdf_file:
        pdf_reader = PyPDF2.PdfReader(input_pdf_file)
        
        # Get the total number of pages
        total_pages = len(pdf_reader.pages)
        
        # Iterate through all the pages
        for page_number in range(total_pages):
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_number])
            
            # Create an output file for each page
            output_pdf_path = f"{output_folder}/page_{page_number + 1}.pdf"
            with open(output_pdf_path, 'wb') as output_pdf_file:
                pdf_writer.write(output_pdf_file)
            
            if page_number % 500 == 0:
                print(f"Page {page_number + 1} of {total_pages} has been saved to {output_pdf_path}")


input_pdf_path = './data/Thong_tin_ung_ho_qua_TSK_VCB_0011001932418_tu_01_09_den10_09_2024.pdf'
output_folder = './pages'
split_pdf(input_pdf_path, output_folder)
