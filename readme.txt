PDF Generation and Combination Script
--------------------------------------

This script automates the process of generating PDFs from a list of URLs and combining them into a single PDF document. It utilizes Python libraries such as pdfkit, selenium, and PyPDF2.

Functions:
----------

1. setup_chrome_driver():
    - Sets up the Selenium Chrome WebDriver in headless mode.
    - Returns the WebDriver instance.

2. generate_pdf_from_url(url, output_pdf):
    - Generates a PDF from a given URL.
    - Uses pdfkit to convert the webpage to PDF.
    - Options include a 5-second delay to ensure page rendering completeness.

3. combine_pdfs(pdf_files, output_pdf):
    - Combines multiple PDF files into a single PDF document.
    - Utilizes PyPDF2's PdfFileMerger class for merging.

4. process_urls(urls_to_convert):
    - Processes a list of URLs and generates PDFs for each URL.
    - Utilizes setup_chrome_driver(), generate_pdf_from_url() functions.
    - Prints progress for each URL processed.
    - Returns a list of generated PDFs.

5. clean_up_files(files):
    - Cleans up temporary files generated during the process.

Main Execution:
---------------

- The main code block initializes the pdfkit configuration for wkhtmltopdf.
- Defines a list of URLs to convert into PDFs.
- Executes the process_urls() function to generate PDFs from the URLs.
- Combines the generated PDFs into a single PDF using combine_pdfs() function.
- Cleans up temporary PDF files using clean_up_files() function.
- Prints a success message upon completion or an error message if an exception occurs.

Note:
-----

- Adjustments can be made to the URLs list and configuration options according to specific requirements.
- Error handling is implemented to catch and print any exceptions that may occur during execution.
