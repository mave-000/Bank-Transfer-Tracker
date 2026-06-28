
import pdfplumber

PDF_FILE = r"C:\Users\user\Desktop\Bank_Statment.pdf"

with pdfplumber.open(PDF_FILE) as pdf:
    for i, page in enumerate(pdf.pages[:3]):
        print(f"\n{'='*50}")
        print(f"PAGE {i+1}")
        print(f"{'='*50}")
        text = page.extract_text()
        if text:
            print(text)
        else:
            print("No text found on this page")