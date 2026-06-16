from reportlab.lib.pagesizes import A3, A4
from reportlab.pdfgen import canvas
import os
import csv
import sys
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from svglib.svglib import svg2rlg, load_svg_file, SvgRenderer
from reportlab.graphics import renderPDF
from reportlab.lib.colors import yellow, green, red, black, HexColor
from reportlab.lib.colors import tan, black, green
from reportlab.lib.units import inch, cm, mm
from math import pi, cos, sin, radians, sqrt

def scaleSVG(svgfile, scaling_factor):
    svg_root = load_svg_file(svgfile)
    svgRenderer = SvgRenderer(svgfile)
    drawing = svgRenderer.render(svg_root)
    scaling_x = scaling_factor
    scaling_y = scaling_factor
    drawing.width = drawing.minWidth() * scaling_x
    drawing.height = drawing.height * scaling_y
    drawing.scale(scaling_x, scaling_y)
    return drawing
    
def create_pdf_template(filename, pagesize, title="Template"):
    """
    Creates a blank PDF template with a title.
    
    :param filename: Output PDF file name
    :param pagesize: Tuple (width, height) in points
    :param title: Title text to display on the page
    """
    try:
        c = canvas.Canvas(filename, pagesize=pagesize)
        width, height = pagesize

        # Draw title at the top center
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(width / 2, height - 50, title)

        # Optional: Draw border
        c.setLineWidth(1)
        c.setFillColor(HexColor('#ff0000'))
        c.rect(20, 20, width - 40, height - 40, fill=1, stroke=1)
        drawing = scaleSVG('SVG/Plus_symbol.svg', 1.0)    
        renderPDF.draw(drawing, c, 150, 475)

        c.showPage()
        c.save()
        print(f"✅ PDF template '{filename}' created successfully.")
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")

if __name__ == "__main__":
    os.makedirs("templates", exist_ok=True)

    # Create A4 template
    create_pdf_template("PDF/template_A4.pdf", A4, title="A4 Template")

    # Create A3 template
    create_pdf_template("PDF/template_A3.pdf", A3, title="A3 Template")
