# table_with_images.py
import os
import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Paragraph, Image

def table_with_images():
    doc = SimpleDocTemplate("PDF/table_with_images.pdf", pagesize=portrait(A4))
    story = []
    styles = getSampleStyleSheet()

    img = Image("Cover.jpg", 50, 50)

    ptext = 'This is some <font color=blue size=14>formatted</font> text'
    p = Paragraph(ptext, styles['Normal'])

    data = [['col_{}'.format(x) for x in range(1, 6)],
            [p for x in range(1, 6)],
            [img, img, img, img, img]
            ]

    tblstyle = TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                           ])

    tbl = Table(data)
    tbl.setStyle(tblstyle)
    story.append(tbl)

    doc.build(story)

if __name__ == '__main__':
    if sys.platform[0] == 'l':
        path = '/home/jan/git/ReportLAB'
    if sys.platform[0] == 'w':
        path = "C:/Users/janbo/OneDrive/Documents/GitHub/ReportLAB"
    os.chdir(path)
    key = input("Wait")
    table_with_images()
    key = input("Wait")