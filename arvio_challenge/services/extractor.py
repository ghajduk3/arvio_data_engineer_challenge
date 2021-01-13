from io import StringIO,BytesIO
from pdfminer.high_level import extract_text_to_fp,extract_text
from pdfminer.layout import LAParams
from lxml import html
import re

class Extractor:

    def extract_text(self,pdf_content):
        return extract_text(BytesIO(pdf_content))

    def extract_data(self,pdf_content):
        raw_text = self.extract_text(pdf_content)
        stevilka_iskaznice = re.findall(r"\d{1,}-\d{1,}-\d{1,}-\d{1,}$", raw_text, re.MULTILINE)[0]
        katastrska_obcina = re.findall(r"katastrska občina \d+$", raw_text, re.MULTILINE)[0].split(' ')[2]
        stevilka_stavbe = re.findall(r"številka stavbe \d+$", raw_text, re.MULTILINE)[0].split(' ')[2]
        razred_ext = re.findall(r"Razred [A-Z]?\d?", raw_text, re.MULTILINE)
        razred = razred_ext[0].split(' ')[1] if len(razred_ext)>0 else 'N'
        deli_stavbe =  re.findall(r"deli? stavbe((( \d+(,|\n|$))+(\n|$))?((\d+,( |\n))+(\d+)| \d+)?)$",raw_text,re.MULTILINE)
        deli_stavbe_refactored = [int(x) for x in ','.join(deli_stavbe[0]).strip().replace('\n', ' ').replace(' ', '').split(',') if
                x != '']
        return stevilka_iskaznice,katastrska_obcina,stevilka_stavbe,deli_stavbe_refactored,razred


