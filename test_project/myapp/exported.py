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
    line = 2

    def __creating_an_empty_table(column_names, file):
        '''
        Функция принимает список названий столбцов - column_names и объект - file
        типа Workbook(), создавая нужную пустую таблицу
        '''

        for col_num, header in enumerate(column_names, 1):
                file.cell(row=1, column=col_num, value=header)
        return ws
    
    def __filling_out_table_fields(data_arr):
        '''
        Функция принимает массив данных конкретного объекта - data_arr
        и поколоночно записывает данные в цикле 
        '''

        for col_num in range(len(data_arr)):
            ws.cell(row=line, column = col_num + 1, value = data_arr[col_num])
        
    
    match data_model.lower():
        case 'countries':
            # задаем имя файла экспорта
            output_file = 'countries.xlsx'
            # генерируем пустую таблицу нужными названиями столбцов
            ws = __creating_an_empty_table(['Страны'], ws)
            # перебор обьектов модели и запись в файл
            for country in Country.objects.all(): 
                __filling_out_table_fields(str(country).split(' '))
                line += 1

        case 'manufacturers':
            output_file = 'manufacturers.xlsx'
            ws = __creating_an_empty_table(['Модель', 'Страна'], ws)
           
            for manufacturer in  Manufacturer.objects.all(): 
                __filling_out_table_fields(manufacturer._for_export().split('|'))
                line += 1

        case 'cars':
            output_file = 'cars.xlsx'
            ws = __creating_an_empty_table(['Автомобиль', 'Производитель', 'Страна', 'Год начала выпуска', 'Год окончания выпуска'], ws)

            for car in  Car.objects.all():
                print(type(car))
                __filling_out_table_fields(car._for_export().split('|'))
                line += 1

        case 'comments':
            output_file = 'comments.xlsx'
            ws = __creating_an_empty_table(['e-mail', 'Дата комментария', 'Автомобиль', 'Комментарий'], ws)

            for comment in  Comment.objects.all():
                print(type(comment))
                __filling_out_table_fields(comment._for_export().split('|'))
                line += 1                       
        case _:
            return HttpResponse('<h1>Invalid request</h1>')

    # сохраняем итоговый файл
    wb.save(output_file)
    # Возвращение файла xlsx в ответе
    with open(output_file, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        # в последующем можно удалить 
        response['Content-Disposition'] = 'attachment; filename="{0}".xlsx'.format(os.path.basename(output_file))
        return response