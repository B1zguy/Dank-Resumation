### WORKING ###

from docxtpl import DocxTemplate

le_docx = 'example-resumation.docx'
# le_docx = 'quick-test.docx'
doc = DocxTemplate(le_docx)
context = { 'yeet' : 'LOPI',
            'nether': 'POLI',
            'date': 'bahaha',
            'too': 'YAYYY'}
doc.render(context)
# set_vars = doc.get_undeclared_template_variables()
# print(set_vars)
doc.save(le_docx)