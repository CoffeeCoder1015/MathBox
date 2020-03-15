from pydocx import PyDocX
from bs4 import BeautifulSoup

docx_FILE = input("docxFile:")
ouput_HTML = input("Outputfile:")

html = PyDocX.to_html(docx_FILE)
html=BeautifulSoup(html,'html.parser')
html=html.prettify('utf-8')
with open(ouput_HTML+".html","wb") as fIO:
    fIO.write(html)