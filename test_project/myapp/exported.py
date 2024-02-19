from django.http import HttpResponse
from .models import *
import os
from django.http import HttpResponse
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from django.forms.models import model_to_dict



def export_to_xlsx(request, data_model = None):

    wb = Workbook()
    ws = wb.active
    
    match data_model.lower():

        case 'country':
            output_file = 'output_country.xlsx'
            line = 2
            # Заголовки столбцов
            headers = ['Страны']
            # Добавление заголовков в таблицу
            for col_num, header in enumerate(headers, 1):
                ws.cell(row=1, column=col_num, value=header)
            # Запись в файл
            for country in Country.objects.all():
                ws[f'A{line}'] = str(country)
                line += 1
            wb.save(output_file)

        case 'manufacturer':
            output_file = 'output_manufacturer.xlsx'
            line = 2
            # Заголовки столбцов
            headers = ['Модель', 'Страна']
            # Добавление заголовков в таблицу
            for col_num, header in enumerate(headers, 1):
                ws.cell(row=1, column=col_num, value=header)

            for man in  Manufacturer.objects.all():
                print(man, type(man))


            wb.save(output_file)



    # Возвращение файла xlsx в ответе
    with open(output_file, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="{0}".xlsx'.format(os.path.basename(output_file))
        return response







