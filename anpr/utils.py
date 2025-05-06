# anpr/utils.py

from openpyxl import Workbook
from openpyxl.drawing.image import Image as ExcelImage
import os

def generate_excel_with_images(text_image_list, excel_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "ANPR Report"
    ws.column_dimensions['A'].width = 40
    ws.column_dimensions['B'].width = 50

    ws.append(["Detected Text", "Frame Image"])

    for text, image_path in text_image_list:
        ws.append([text])
        img = ExcelImage(image_path)
        img.width = 200
        img.height = 120
        ws.add_image(img, f'B{ws.max_row}')
    
    wb.save(excel_path)
