# from docx import Document
from docxtpl import DocxTemplate as Document
from docx2pdf import convert as convert_to_pdf
from .utils import generate_string, convert_date
from collections import defaultdict


def replace_text_in_paragraph(paragraph, key, value):
    if key in paragraph.text:
        inline = paragraph.runs
        for item in inline:
            if key in item.text:
                item.text = item.text.replace(key, value)


class DocumentGenerator:
    def __init__(self, name):
        self.document = Document(name)

    def generate_hike_letter(self, output_file_path, details):
        details = defaultdict(lambda: "-", details)
        variables = {
            "CURRENT_DATE": convert_date(details["curr_date"]),
            "EMP_NAME": details["emp_name"],
            "EMP_ID": details["emp_id"],
            "EMP_DESIG": details["emp_designation"],
            "EMP_DEPT": details["emp_dept"],
            "DOJ": convert_date(details["join_date"]),
            "DOL": convert_date(details["leave_date"]),
        }

        template_document = self.document
        template_document.render(variables)
        template_document.save(output_file_path)

    def generate_rel_letter(self, output_file_path, details):
        details = defaultdict(lambda: "-", details)
        variables = {
            "CURRENT_DATE": convert_date(details["curr_date"]),
            "EMP_NAME": details["emp_name"],
            "EMP_ID": details["emp_id"],
            "EMP_DESIG": details["emp_designation"],
            "EMP_DEPT": details["emp_dept"],
            "DOJ": convert_date(details["join_date"]),
            "DOL": convert_date(details["leave_date"]),
        }

        template_document = self.document
        template_document.render(variables)
        template_document.save(output_file_path)

    def generate_payslip_letter(self, output_file_path, details):
        details = defaultdict(lambda: "-", details)
        variables = {
            "CURRENT_DATE": convert_date(details["curr_date"]),
            "EMP_NAME": details["emp_name"],
            "EMP_ID": details["emp_id"],
            "EMP_DESIG": details["emp_designation"],
            "EMP_DEPT": details["emp_dept"],
            "DOJ": convert_date(details["join_date"]),
            "DOL": convert_date(details["leave_date"]),
        }

        template_document = self.document
        template_document.render(variables)
        template_document.save(output_file_path)

    def generate_exp_letter(self, output_file_path, details):
        details = defaultdict(lambda: "-", details)
        variables = {
            "CURRENT_DATE": convert_date(details["curr_date"]),
            "EMP_NAME": details["emp_name"],
            "EMP_ID": details["emp_id"],
            "EMP_DESIG": details["emp_designation"],
            "EMP_DEPT": details["emp_dept"],
            "DOJ": convert_date(details["join_date"]),
            "DOL": convert_date(details["leave_date"]),
        }

        template_document = self.document
        template_document.render(variables)
        template_document.save(output_file_path)

    def generate_offer_letter(self, output_file_path, details):
        details = defaultdict(lambda: "-", details)
        variables = {
            "CURRENT_DATE": convert_date(details["curr_date"]),
            "EMP_NAME": details["emp_name"],
            "EMP_ID": details["emp_id"],
            "EMP_DESIG": details["emp_designation"],
            "EMP_DEPT": details["emp_dept"],
            "DOJ": convert_date(details["join_date"]),
            "DOL": convert_date(details["leave_date"]),
        }

        template_document = self.document
        template_document.render(variables)
        template_document.save(output_file_path)

    def generate_resignation_letter(self, output_file_path, details):
        details = defaultdict(lambda: "-", details)
        variables = {
            "CURRENT_DATE": convert_date(details["curr_date"]),
            "EMP_NAME": details["emp_name"],
            "EMP_ID": details["emp_id"],
            "EMP_DESIG": details["emp_designation"],
            "EMP_DEPT": details["emp_dept"],
            "DOJ": convert_date(details["join_date"]),
            "DOL": convert_date(details["leave_date"]),
        }

        template_document = self.document
        template_document.render(variables)
        template_document.save(output_file_path)

    def generate_pdf(self, input, output):
        convert_to_pdf(input, output)
