import PyPDF2
import io

def extract_text_from_pdf(pdf_file):
    text = ""
    try:
        with io.BytesIO(pdf_file.read()) as f:
            reader = PyPDF2.PdfReader(f)
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
    except PyPDF2.utils.PdfReadError:
        return "Error: Unable to extract text from the PDF."
    return text
