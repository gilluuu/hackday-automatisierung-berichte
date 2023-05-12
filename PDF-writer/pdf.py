from fpdf import FPDF

# Define the page size
page_width = 595.28
page_height = 841.89

# Create a PDF object
pdf = FPDF(unit="pt", format=(page_width, page_height))

# Set the margins
pdf.set_margins(30, 30, 30)

# Set the auto page break
pdf.set_auto_page_break(True, 30)

# Add a new page to the PDF
pdf.add_page()

# Set the font and font size
pdf.set_font("Arial", size=12)

a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
g = "g"

# Create a list of variables containing the text
text_variables = [a, b, c, d, e, f, g]

# Loop through the text variables and add the text to the PDF
for text_variable in text_variables:
    # Split the text into lines
    lines = text_variable.split("\n")
    
    # Loop through the lines and add them to the PDF
    for line in lines:
        # Add the line to the PDF
        pdf.cell(0, pdf.font_size, line)
        pdf.ln()
    
# Save the PDF
pdf.output("my_document.pdf")