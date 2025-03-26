# Assignment 1: Extracting Text from Encrypted PDFs

## Problem Statement
The task was to extract text from an encrypted PDF file without converting it to images or using OCR. The PDF contained tabular data and required handling encryption to access its content.

## Solution Approach
To solve this problem, the following steps and methods were used:

1. **Handling Encrypted PDFs**:
   - The `PyMuPDF` (`fitz`) library was used to open and process the PDF.
   - The `doc.is_encrypted` property was checked to determine if the PDF was encrypted.

2. **Text Extraction**:
   - Once the PDF was decrypted, the `page.get_text("text")` method was used to extract text from each page of the PDF.
   - This method retrieves the text in a structured format, preserving the layout as much as possible.

3. **Processing Extracted Text**:
   - The extracted text was processed line by line to structure it into rows and columns.
   - Each line was split based on delimiters (e.g., colons `:`) to separate keys and values.

4. **Saving Data to Excel**:
   - The structured data was converted into a `pandas.DataFrame`.
   - The DataFrame was then saved to an Excel file using the `pandas.to_excel()` method.

## Tools and Libraries Used
- **PyMuPDF (`fitz`)**: For handling encrypted PDFs and extracting text.
- **pandas**: For structuring the extracted text into a tabular format and saving it to an Excel file.

## Key Features of the Solution
- **Decryption Support**: The solution handles encrypted PDFs by authenticating with a password.
- **Text Structuring**: Extracted text is processed into a clean tabular format.
- **Excel Export**: The final structured data is saved as an Excel file for easy analysis.

## How to Run the Code
1. Install the required libraries:
   ```bash
   pip install pymupdf pandas openpyxl