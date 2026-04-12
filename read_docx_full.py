import docx
import sys
from docx.document import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph

def iter_block_items(parent):
    if isinstance(parent, Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

def read_docx(file_path):
    doc = docx.Document(file_path)
    text = []
    for block in iter_block_items(doc):
        if isinstance(block, Paragraph):
            text.append(block.text)
        elif isinstance(block, Table):
            for row in block.rows:
                row_data = []
                for cell in row.cells:
                    row_data.append(cell.text.replace('\n', ' '))
                text.append(' | '.join(row_data))
    return '\n'.join(text)

if __name__ == '__main__':
    text = read_docx(sys.argv[1])
    with open('docx_content_full.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Success")
