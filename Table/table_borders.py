import os
import sys
from reportlab.platypus import (
    BaseDocTemplate,
    PageTemplate,
    Frame,
    Table,
    TableStyle
)
from reportlab.lib import colors


def stylesheet():
    return {
        'table_default': TableStyle(
            [
                ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.gray),
                ('INNERGRID', (1, 1), (2, 2), 0.5, colors.green),
                ('BACKGROUND', (0, 0), (-1, -1), colors.yellow),
                ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                ('BOX', (1, 1), (2, 2), 0.5, colors.green),
                ('BOX', (0, 0), (1, 1), 1, colors.red),

            ]
        ),
    }


def build_flowables(stylesheet):
    return [
        Table(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            style=stylesheet['table_default'],
        )
    ]


def build_pdf(filename, flowables):
    doc = BaseDocTemplate(filename)
    doc.addPageTemplates(
        [
            PageTemplate(
                frames=[
                    Frame(
                        doc.leftMargin,
                        doc.bottomMargin,
                        doc.width,
                        doc.height,
                        id=None
                    ),
                ]
            ),
        ]
    )
    doc.build(flowables)

if sys.platform[0] == 'l':
    path = '/home/jan/git/ReportLAB'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/ReportLAB"
os.chdir(path)
key = input("Wait")
build_pdf('PDF/p0156_1.pdf', build_flowables(stylesheet()))
