from operator import itemgetter

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, \
    Table, TableStyle

class DataToPdf():

    def __init__(self, fields, data, parts, sort_by=None, title=None, username = None, name=None, date = None):
        self.fields = fields
        self.data = data
        self.title = title
        self.sort_by = sort_by
        self.parts = parts
        self.name = name
        self.username = username
        self.date = date

    def export(self, filename, data_align='LEFT', table_halign='LEFT'):

        doc = SimpleDocTemplate(filename, pagesize=landscape(letter))

        styles = getSampleStyleSheet()
        styleH = styles['Heading1']

        story = []

        if self.title:
            story.append(Paragraph(self.username+'\n', styleH))
            story.append(Paragraph(self.date + '\n', styleH))
            story.append(Paragraph(self.name+'\n', styleH))
            story.append(Paragraph(self.title+'\n', styleH))
            story.append(Spacer(1, 0.25 * inch))

        converted_data = self.__convert_data()
        table = Table(converted_data, hAlign=table_halign)
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('ALIGN', (0, 0), (-1, 0), 'LEFT'),
            ('ALIGN',(0, 0),(0,-1), data_align),
            ('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
        ]))

        story.append(table)

        for i in range(0,len(self.parts)):
             story.append(self.parts[i])
        doc.build(story)

    def __convert_data(self):

        keys, names = zip(*[[k, n] for k, n in self.fields])
        new_data = [names]

        for d in self.data:
            new_data.append([d[k] for k in keys])

        return new_data