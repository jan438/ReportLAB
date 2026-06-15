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
from reportlab.lib.colors import yellow, green, red, black, gray, white, HexColor, tan
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

    try:
        c = canvas.Canvas(filename, pagesize=pagesize)
        width, height = pagesize

        # Draw title at the top center
        c.setFont("Helvetica-Bold", 24)
        c.drawCentredString(width / 2, height - 50, title)

        # Optional: Draw border
        c.setLineWidth(1)
        c.rect(20, 20, width - 40, height - 40)
        renderPDF.draw(scaleSVG("star.svg", 50.0), c, 0, 0)

        c.showPage()
        c.save()
        print(f"✅ PDF template '{filename}' created successfully.")
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")


create_pdf_template("PDF/startodocrop.pdf", A4, title="Star")

key = input("Wait")
