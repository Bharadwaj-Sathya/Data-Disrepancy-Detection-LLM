from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import random

# Sample product names
PRODUCT_NAMES = ['Laptop', 'Smartphone', 'Tablet', 'Camera', 'Headphones', 'Smartwatch', 'Television', 'Printer',
                 'Router', 'Speaker']


def generate_sample_pdf(file_name, invoice_data, discount_percentage):
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    elements = []

    # Define table data (sample invoice data)
    data = [
        ['Item', 'Quantity', 'Price', f'Discount ({discount_percentage}%)', 'Total']]  # Added column: 'Discount (10%)'
    num_items = min(random.randint(10, 15), len(PRODUCT_NAMES))  # Ensure at least 10 unique items
    items = random.sample(PRODUCT_NAMES, num_items)  # Choose random items without repetition
    total_discount = 0
    for item in items:
        quantity = random.randint(1, 10)
        price = round(random.uniform(10, 100), 2)
        discount = round(price * quantity * (discount_percentage / 100), 2)
        total_discount += discount
        total = round(price * quantity - discount, 2)
        data.append([item, quantity, price, discount, total])

    # Add table to the PDF
    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    elements.append(table)

    # Add additional information (invoice data) as Paragraphs
    styles = getSampleStyleSheet()
    for key, value in invoice_data.items():
        details_paragraph = Paragraph(f"{key}: {value}", styles['Normal'])
        value_paragraph = Paragraph(str(value), styles['Normal'])
        elements.extend([details_paragraph])

    # Build the PDF
    doc.build(elements)


# Generate multiple sample PDF invoices
num_invoices = 5  # Change this value to generate the desired number of invoices
for i in range(0, num_invoices):
    file_name = f"./data/input/invoice_{i}.pdf"
    invoice_data = {
        "Invoice Number": f"INV00{i}",
        "Customer Name": f"Customer_{i}",
        # Add more invoice data fields if needed
    }
    discount_percentage = random.randint(8, 12)
    generate_sample_pdf(file_name, invoice_data, discount_percentage)
    print(f"Generated PDF invoice: {file_name}")
