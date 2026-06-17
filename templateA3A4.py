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
    
def drawfont(i, c, name):
    c.setFillColor(HexColor("#ffffff"))
    c.setFont(name, 30)
    c.drawString(100, 950 - i * 92, "ABCDEFGHIJKLMNOPQRSTUVVWXYZ")
    c.drawString(100, 925 - i * 92, "abcdefghijklmnopqrstuvwxyz")
    c.setFont(name, 22)
    c.drawString(100, 895 - i * 92, name)
    
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
        # Optional: Draw border
        c.setLineWidth(1)
        c.setFillColor(HexColor("#000000"))
        c.setStrokeColor(HexColor("#ffffff"))
        c.rect(20, 20, width - 40, height - 40, fill=1, stroke=1)
        # Draw title at the top center
        c.setFont("Helvetica-Bold", 24)
        c.setFillColor(HexColor("#ffffff"))
        c.drawCentredString(width / 2, height - 50, "hallohallo")
        drawing = scaleSVG('SVG/star.svg', 1.0)
        renderPDF.draw(drawing, c, -500, -100)
        drawfont(0, c, "Arial")
        drawfont(1, c, "Verdana")
        drawfont(2, c, "Georgia")
        drawfont(3, c, "TimesNewRoman")
        drawfont(4, c, "Trebuchet")
        drawfont(5, c, "Ubuntu")
        drawfont(6, c, "DejaVuSerif")
        drawfont(7, c, "LiberationSerif")   
        drawfont(8, c, "DancingScript")
        drawfont(9, c, "CormorantGaramond")
        c.showPage()
        c.save()
        print(f"✅ PDF template '{filename}' created successfully.")
    except Exception as e:
        print(f"❌ Error creating PDF: {e}")

if __name__ == "__main__":
    if sys.platform[0] == 'l':
        path = '/home/jan/git/ReportLAB'
    if sys.platform[0] == 'w':
        path = "C:/Users/janbo/OneDrive/Documents/GitHub/ReportLAB"
    os.chdir(path)
    os.makedirs("templates", exist_ok=True)
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
    pdfmetrics.registerFont(TTFont('ArialBold', 'Arial_Bold.ttf'))
    pdfmetrics.registerFont(TTFont('ArialItalic', 'Arial_Italic.ttf'))
    pdfmetrics.registerFont(TTFont('ArialBoldItalic', 'Arial_Bold_Italic.ttf'))
    pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
    pdfmetrics.registerFont(TTFont('VerdanaBold', 'Verdana_Bold.ttf'))
    pdfmetrics.registerFont(TTFont('VerdanaItalic', 'Verdana_Italic.ttf'))
    pdfmetrics.registerFont(TTFont('VerdanaBoldItalic', 'Verdana_Bold_Italic.ttf'))
    pdfmetrics.registerFont(TTFont('Georgia', 'Georgia.ttf'))
    pdfmetrics.registerFont(TTFont('GeorgiaBold', 'Georgia_Bold.ttf'))
    pdfmetrics.registerFont(TTFont('GeorgiaItalic', 'Georgia_Italic.ttf'))
    pdfmetrics.registerFont(TTFont('GeorgiaBoldItalic', 'Georgia_Bold_Italic.ttf'))
    pdfmetrics.registerFont(TTFont('TimesNewRoman', 'times.ttf'))
    pdfmetrics.registerFont(TTFont('TimesNewRomanBold', 'timesbd.ttf'))
    pdfmetrics.registerFont(TTFont('TimesNewRomanItalic', 'timesi.ttf'))
    pdfmetrics.registerFont(TTFont('TimesNewRomanBoldItalic', 'timesbi.ttf'))
    pdfmetrics.registerFont(TTFont('Trebuchet', 'Trebuchet_MS.ttf'))
    pdfmetrics.registerFont(TTFont('TrebuchetBold', 'Trebuchet_MS_Bold.ttf'))
    pdfmetrics.registerFont(TTFont('TrebuchetItalic', 'Trebuchet_MS_Italic.ttf'))
    pdfmetrics.registerFont(TTFont('TrebuchetBoldItalic', 'Trebuchet_MS_Bold_Italic.ttf'))
    pdfmetrics.registerFont(TTFont('Ubuntu', 'Ubuntu-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('UbuntuBold', 'Ubuntu-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('UbuntuItalic', 'Ubuntu-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('UbuntuBoldItalic', 'Ubuntu-BoldItalic.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSerifBold', 'DejaVuSerif-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSerifItalic', 'DejaVuSerif-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSerifBoldItalic', 'DejaVuSerif-BoldItalic.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSerif', 'LiberationSerif-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSerifBold', 'LiberationSerif-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSerifItalic', 'LiberationSerif-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('LiberationSerifBoldItalic', 'LiberationSerif-BoldItalic.ttf'))
    pdfmetrics.registerFont(TTFont('DancingScript', 'DancingScript-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('DancingScriptBold', 'DancingScript-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('DancingScriptItalic', 'DancingScript-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('DancingScriptBoldItalic', 'DancingScript-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('CormorantGaramond', 'CormorantGaramond-Regular.ttf'))
    pdfmetrics.registerFont(TTFont('CormorantGaramondBold', 'CormorantGaramond-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('CormorantGaramondItalic', 'CormorantGaramond-Italic.ttf'))
    pdfmetrics.registerFont(TTFont('CormorantGaramondBoldItalic', 'CormorantGaramond-BoldItalic.ttf'))
    # Create A4 template
    create_pdf_template("PDF/template_A4.pdf", A4, title="A4 Template")
    # Create A3 template
    create_pdf_template("PDF/template_A3.pdf", A3, title="A3 Template")
