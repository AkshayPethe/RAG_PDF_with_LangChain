from PyPDF2 import PdfReader


def get_pdf_text(pdf_docs):
    try:
        text = ""
        pdf_reader = PdfReader(pdf_docs)
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
            print(f"An error occurred while extracting text from PDF: {e}")
            return None
