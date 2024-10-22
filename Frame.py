from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import *

if __name__ == "__main__":
    style_1 = ParagraphStyle(name='Stylo',
                              fontName='Helvetica',
                              fontSize=20,
                              leading=12)
    doc = BaseDocTemplate('PDF/test_spacer.pdf', showBoundary=1, 
                             pagesize=landscape(A4), topMargin=30,
                           bottomMargin=30,
                           leftMargin=30, rightMargin=30)

    frameCount = 2
    frameWidth = (doc.width) / frameCount
    frameHeight = doc.height - .05 * inch
    frames = []
    column = Frame(doc.leftMargin, doc.bottomMargin, 200, doc.height - .05* inch)
    frames.append(column)
    column = Frame(doc.leftMargin + 200, doc.bottomMargin, frameWidth - 200, doc.height - .05 * inch)
    frames.append(column)
    doc.addPageTemplates([PageTemplate(id='framess', frames=frames)])
    story = []
    for i, x in enumerate(['A', 'B', 'C']):
        text = x*10*(i+1)
        print(text)
        p1 = Paragraph(text, style_1)
        w, h1 = p1.wrap(200, doc.height)
        p2 = Paragraph(text*2, style_1)
        w, h2 = p2.wrap(200, doc.height)
        story.append(p1)
        story.append(p2)
        spac_height = ((doc.height) - (h1 + h2))
        story.append(Spacer(width=0, height=spac_height))
        story.append(Paragraph('This should be on the top of the 2nd Frame!' + x, style_1))
        story.append(PageBreak())
    key = input("WaitForBuild")
    try:
        doc.build(story)
    except Exception as err:
        print("Doc build failed", err)
    key = input("WaitFinal")