from datetime import datetime
from django.http import HttpResponse
from rest_framework.response import Response
from openpyxl import Workbook
import csv, io



class ExportDataToCsvOrXlsx():
    '''
    Класс экспорта данных различных моделей в файл формата csv-xlsx 
    в зависимости от переданного в GET-запросе параметра 
    '''
    
    def __init__(self, request, queryset, attributs, data_format):
        self.queryset = queryset
        self.attributs = attributs
        self.data_format = data_format
        self.request = request


    def get_file(self):
        if self.data_format == 'csv':
            return self.export_to_csv(self.request)
        elif self.data_format == 'xlsx':
             return self.export_to_xlsx(self.request)
        else:
            return Response({'Error':'An incorrect value for the "get" parameter was passed'}) 


    def export_to_xlsx(self, request):
        wb = Workbook()
        ws = wb.active

        ws.append(self.attributs)

        for instance in self.queryset:
            instance_data = [str(getattr(instance, attr)) for attr in self.attributs]
            ws.append(instance_data)
           
        output = io.BytesIO()
        wb.save(output)
        output.seek(0)

        self.response = HttpResponse(
            output.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        self.filename_generate(self.response, data_type='xlsx')

        return self.response


    def export_to_csv(self, request):
        self.response = HttpResponse(content_type='text/csv')
        self.filename_generate(self.response, data_type='csv')

        writer = csv.writer(self.response)

        writer.writerow(self.attributs)

        for instance in self.queryset:
            instance_data = [str(getattr(instance, attr)) for attr in self.attributs]
            writer.writerow(instance_data)

        return self.response
    

    def filename_generate(self, response, data_type):
        self.response['Content-Disposition'] = f'attachment;\
        filename="{self.queryset.model._meta.model_name} {str(datetime.now().date())} {str(datetime.now().time())[:5]}.{data_type}"'
    