# absolute_pos_flowable.py
import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def background(c):
    c.setFillColorRGB(1,0,0)
    c.rect(5,5,652,792,fill=1)

def mixed():
    my_canvas = canvas.Canvas("PDF/mixed_flowables.pdf", pagesize=letter)
    background(my_canvas)
    styles = getSampleStyleSheet()
    width, height = letter
    text = "Hello, I'm a Paragraph"
    para = Paragraph(text, style=styles["Normal"])
    para.wrapOn(my_canvas, width, height)
    para.drawOn(my_canvas, 20, 760)
    my_canvas.save()

if __name__ == '__main__':
    if sys.platform[0] == 'l':
        path = '/home/jan/git/ReportLAB'
    if sys.platform[0] == 'w':
        path = "C:/Users/janbo/OneDrive/Documents/GitHub/ReportLAB"
    os.chdir(path)
    mixed()
    key = input("Wait")
