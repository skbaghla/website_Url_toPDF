import os
import time
import pdfkit
from selenium import webdriver
from PyPDF2 import PdfFileMerger

def setup_chrome_driver():
    """Set up Selenium Chrome WebDriver."""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Run Chrome in headless mode
    return webdriver.Chrome(options=chrome_options)

def generate_pdf_from_url(url, output_pdf):
    """Generate PDF from URL."""
    options = {
        'javascript-delay': 5000,  # Wait for 5 seconds for page to render completely
    }
    pdfkit.from_url(url, output_pdf, configuration=config, options=options)

def combine_pdfs(pdf_files, output_pdf):
    """Combine multiple PDF files into a single PDF."""
    merger = PdfFileMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    merger.write(output_pdf)
    merger.close()

def process_urls(urls_to_convert):
    """Process a list of URLs and generate PDFs."""
    output_pdfs = []
    driver = setup_chrome_driver()
    try:
        for index, url in enumerate(urls_to_convert):
            output_pdf = f"output_{index}.pdf"
            driver.get(url)
            time.sleep(5)  # Wait for page to fully load
            driver.save_screenshot(f"screenshot_{index}.png")  # Optional: Take screenshot for debugging
            generate_pdf_from_url(url, output_pdf)
            output_pdfs.append(output_pdf)
            print(f"Processed URL {index + 1}/{len(urls_to_convert)}")
    finally:
        driver.quit()
    return output_pdfs

def clean_up_files(files):
    """Clean up temporary files."""
    for file in files:
        os.remove(file)

if __name__ == '__main__':
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    urls_to_convert = [
        "https://www.linkedin.com/in/skbaghla/",
        "https://github.com/skbaghla",
    ]
    try:
        output_pdfs = process_urls(urls_to_convert)
        output_combined_pdf = "combined_output.pdf"
        combine_pdfs(output_pdfs, output_combined_pdf)
        clean_up_files(output_pdfs)
        print("PDF generation and combination completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
