import csv
import re
import threading
import pandas as pd
import xlwt
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.encoding import smart_str
from requests import Response
from rest_framework.decorators import api_view
from .googledriveprocces import GoogleDrive
from .models import (
    DataFormTable,
    Pacient,
    gen_aaaannnna,
    UserProfile,
    User,
    ProfileFormTable,
    Drug,
    MedicalOperation,
    ChldPacientDurBreast,
    RelationhipPacient,
    Cancer, CancerHistory, DataDictionary
)

import jbssys.validators as vaidator_data


def master_tableLoadFile(request):
    if request.method =='GET':

        return

def pacientDownLoadFile(request):
    pass


def master_tableDownloadFileTemps(request):
    if request.method == "GET":
        columns_names1 = ['Create', 'First Name', 'Surname', 'Date of birth', 'Client phone',
                         'NHS ID', 'Screener', 'Datapoint 8', 'Datapoint 9', 'Datapoint 10',
                         'Datapoint 11', 'Datapoint 12', 'Datapoint 13', 'Datapoint 14', 'Datapoint 15',
                         'Datapoint 16', 'Datapoint 16A', 'Datapoint 16B', 'Datapoint 17', 'Datapoint 18',
                         'Datapoint 19', 'Datapoint 20',
                         'Datapoint 21', 'Datapoint 22', 'Datapoint 23', 'Datapoint 24', 'Datapoint 25',
                         'Datapoint 26', 'Datapoint 27', 'Datapoint 28', 'Datapoint 29', 'Datapoint 30',
                         'Datapoint 31', 'Datapoint 32', 'Datapoint 33', 'Datapoint 34', 'Datapoint 35',
                         'Datapoint 36', 'Datapoint 37', 'Datapoint 38', 'Datapoint 39', 'Datapoint 40',
                         'Datapoint 41', 'Datapoint 42', 'Datapoint 43', 'Datapoint 44', 'Datapoint 45',
                         'Datapoint 46', 'Datapoint 47', 'Datapoint 48', 'Datapoint 49', 'Datapoint 50',
                         'Datapoint 51', 'Datapoint 52', 'Datapoint 53', 'Datapoint 54', 'Datapoint 55',
                         'Datapoint 56', 'Datapoint 57', 'Datapoint 58', 'Datapoint 59', 'Datapoint 60',
                         'Datapoint 61', 'Datapoint 62', 'Datapoint 63', 'Datapoint 64', 'Datapoint 65',
                         'Datapoint 66', 'Datapoint 67', 'Datapoint 68', 'Datapoint 69', 'Datapoint 70',
                         'Datapoint 71', 'Datapoint 72', 'Datapoint 73', 'Datapoint 74', 'Datapoint 75',
                         'Datapoint 76', 'Datapoint 77', 'Datapoint 78', 'Datapoint 79', 'Datapoint 80',
                         'Datapoint 81', 'Datapoint 82', 'Datapoint 83', 'Datapoint 84', 'Datapoint 85',
                         'Datapoint 86', 'Datapoint 87', 'Datapoint 88', 'Datapoint 89', 'Datapoint 90',
                         'Datapoint 91', 'Datapoint 92', 'Datapoint 93', 'Datapoint 94', 'Datapoint 95',
                         'Datapoint 96', 'Datapoint 97', 'Datapoint 98', 'Datapoint 99', 'Datapoint 100',
                         'Datapoint 101', 'Datapoint 102', 'Datapoint 103', 'Datapoint 104', 'Datapoint 105',
                         'Datapoint 106', 'Datapoint 107', 'Datapoint 108', 'Datapoint 109', 'Datapoint 110',
                         'Datapoint 111', 'Datapoint 112', 'Datapoint 113', 'Datapoint 114', 'Datapoint 115',
                         'Datapoint 116', 'Datapoint 117', 'Datapoint 118', 'Datapoint 119','GD id']

        columns_names2 = ['Create', 'First Name', 'Surname', 'Date of birth', 'Client phone',
                          'NHS ID', 'Datapoint 8', 'Datapoint 8', 'Datapoint 9', 'Datapoint 10',
                          'Datapoint 11', 'Datapoint 12', 'Datapoint 13a', 'Datapoint 13b', 'Datapoint 14', 'Datapoint 15',
                          'Datapoint 16', 'Datapoint 17', 'Datapoint 18','Datapoint 19', 'Datapoint 20',
                          'Datapoint 21', 'Datapoint 22', 'Datapoint 23', 'Datapoint 24', 'Datapoint 25',
                          'Datapoint 26', 'Datapoint 27', 'Datapoint 28', 'Datapoint 29', 'Datapoint 30',
                          'Datapoint 31', 'Datapoint 32', 'Datapoint 33', 'Datapoint 34', 'Datapoint 35',
                          'Datapoint 36', 'Datapoint 37', 'Datapoint 38', 'Datapoint 39', 'Datapoint 40',
                          'Datapoint 41', 'Datapoint 42', 'Datapoint 43', 'Datapoint 44', 'Datapoint 45',
                          'Datapoint 46', 'Datapoint 47', 'Datapoint 48', 'Datapoint 49', 'Datapoint 50',
                          'Datapoint 51', 'Datapoint 52', 'Datapoint 53', 'Datapoint 54', 'Datapoint 55',
                          'Datapoint 56', 'Datapoint 57', 'Datapoint 58', 'Datapoint 59', 'Datapoint 60',
                          'Datapoint 61', 'Datapoint 62', 'Datapoint 63', 'Datapoint 64', 'Datapoint 65',
                          'Datapoint 66', 'Datapoint 67', 'Datapoint 68', 'Datapoint 69', 'Datapoint 70',
                          'Datapoint 71', 'Datapoint 72', 'Datapoint 73', 'Datapoint 74', 'Datapoint 75',
                          'Datapoint 76', 'Datapoint 77', 'Datapoint 78', 'Datapoint 79', 'Datapoint 80',
                          'Datapoint 81', 'Datapoint 82', 'Datapoint 83', 'Datapoint 84', 'Datapoint 85',
                          'Datapoint 86', 'Datapoint 87', 'Datapoint 88', 'Datapoint 89', 'Datapoint 90',
                          'Datapoint 91', 'Datapoint 92', 'Datapoint 93', 'Datapoint 94','GD id']


        response = HttpResponse(content_type='application/force-download')

        response['Content-Disposition'] = 'attachment; filename=%s' % 'Data-FormTemp.xlsx'

        response['X-Sendfile'] = 'static/sample_template/Data-FormTemp.xlsx'

        return response

def master_tableDownloadFile(request):
    if request.method =='GET':
        format_file = request.GET.get('format_file')

        format_file = format_file if format_file else 'csv'

        search_param = {}

        first_name = request.GET.get('first_name')

        last_name = request.GET.get('last_name')

        phone = request.GET.get('phone')

        email = request.GET.get('email')

        nsh_id = request.GET.get('nsh_id')

        default_city = request.GET.get('city')

        home_addres = request.GET.get('addres')
        birth_from = request.GET.get('birth_from')

        birth_to = request.GET.get('birth_to')

        if email:
            email = vaidator_data.validate_email(str(email))

            search_param['email'] = email

        if nsh_id:
            nsh_id = str(nsh_id)

            search_param['nsh_id'] = nsh_id

        if first_name:

            search_param['first_name'] = first_name

        if last_name:
            search_param['last_name'] = last_name

        search_param['is_hide'] = False

        if phone:
            phone = vaidator_data.validate_phone(str(phone))

            search_param['phone'] = phone

        if default_city:
            default_city = str(default_city)

            search_param['default_city'] = default_city

        if home_addres:
            home_addres = str(home_addres)

            search_param['home_addres'] = home_addres

        # if birth_from and birth_to:
        #     birth_from = vaidator_data.validate_date(str(birth_from))
        #
        #     search_param['date_of_birth__range'] = [birth_from, birth_to]
        #
        # elif birth_from:
        #     birth_from = vaidator_data.validate_date(str(birth_from))
        #
        #     search_param['date_of_birth__range'] = [birth_from, '2023-12-30']
        #
        # elif birth_to:
        #     birth_to = vaidator_data.validate_date(str(birth_to))
        #
        #     search_param['date_of_birth__range'] = ['1900-01-01',birth_to]
        #
        # else:
        #     search_param['date_of_birth__range'] = ['1900-01-01','2023-12-30']
        master_table = DataFormTable.objects.filter(**search_param).order_by('id')


        columns_names = ['Create', 'First Name', 'Surname', 'Date of birth', 'Client phone',
                         'NHS ID', 'Screener', 'Datapoint 8', 'Datapoint 9', 'Datapoint 10',
                         'Datapoint 11',  'Datapoint 12',  'Datapoint 13',  'Datapoint 14', 'Datapoint 15',
                         'Datapoint 16',  'Datapoint 16A', 'Datapoint 16B', 'Datapoint 17', 'Datapoint 18', 'Datapoint 19', 'Datapoint 20',
                         'Datapoint 21',  'Datapoint 22',  'Datapoint 23',  'Datapoint 24', 'Datapoint 25',
                         'Datapoint 26',  'Datapoint 27',  'Datapoint 28',  'Datapoint 29', 'Datapoint 30',
                         'Datapoint 31',  'Datapoint 32',  'Datapoint 33',  'Datapoint 34', 'Datapoint 35',
                         'Datapoint 36',  'Datapoint 37',  'Datapoint 38',  'Datapoint 39', 'Datapoint 40',
                         'Datapoint 41',  'Datapoint 42',  'Datapoint 43',  'Datapoint 44', 'Datapoint 45',
                         'Datapoint 46',  'Datapoint 47',  'Datapoint 48',  'Datapoint 49', 'Datapoint 50',
                         'Datapoint 51',  'Datapoint 52',  'Datapoint 53',  'Datapoint 54', 'Datapoint 55',
                         'Datapoint 56',  'Datapoint 57',  'Datapoint 58',  'Datapoint 59', 'Datapoint 60',
                         'Datapoint 61',  'Datapoint 62',  'Datapoint 63',  'Datapoint 64', 'Datapoint 65',
                         'Datapoint 66',  'Datapoint 67',  'Datapoint 68',  'Datapoint 69', 'Datapoint 70',
                         'Datapoint 71',  'Datapoint 72',  'Datapoint 73',  'Datapoint 74', 'Datapoint 75',
                         'Datapoint 76',  'Datapoint 77',  'Datapoint 78',  'Datapoint 79', 'Datapoint 80',
                         'Datapoint 81',  'Datapoint 82',  'Datapoint 83',  'Datapoint 84', 'Datapoint 85',
                         'Datapoint 86',  'Datapoint 87',  'Datapoint 88',  'Datapoint 89', 'Datapoint 90',
                         'Datapoint 91',  'Datapoint 92',  'Datapoint 93',  'Datapoint 94', 'Datapoint 95',
                         'Datapoint 96',  'Datapoint 97',  'Datapoint 98',  'Datapoint 99', 'Datapoint 100',
                         'Datapoint 101', 'Datapoint 102', 'Datapoint 103', 'Datapoint 104', 'Datapoint 105',
                         'Datapoint 106', 'Datapoint 107', 'Datapoint 108', 'Datapoint 109', 'Datapoint 110',
                         'Datapoint 111', 'Datapoint 112', 'Datapoint 113', 'Datapoint 114', 'Datapoint 115',
                         'Datapoint 116', 'Datapoint 117', 'Datapoint 118', 'Datapoint 119']


        if format_file == 'csv':



            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="clinical_master_table.csv"'

            writer = csv.writer(response)
            writer.writerow(columns_names)

            for master_data in master_table:
                writer.writerow([
                    str(master_data.create_datetime),
                    master_data.pacient.first_name,
                    master_data.pacient.last_name,
                    str(master_data.pacient.date_of_birth),
                    master_data.pacient.phone,
                    master_data.pacient.nsh_id,
                    master_data.datapoint_7,



                    master_data.get_datapoint8_display(),


                    master_data.get_datapoint_9_display(),

                    master_data.get_datapoint_10_display(),

                    master_data.get_datapoint_11_display(),

                    master_data.get_datapoint_12_display(),


                    master_data.get_datapoint_13_display(),

                    master_data.get_datapoint_14_display(),

                    master_data.get_datapoint15_display(),

                    master_data.get_datapoint16_display(),

                    master_data.get_datapoint_16_b_display(),

                    master_data.get_datapoint_16_b_display(),


                    master_data.get_datapoint_17_display(),

                    master_data.get_datapoint18_display(),
                    master_data.get_datapoint19_display(),

                    master_data.get_datapoint20_display(),


                    master_data.get_datapoint_21_display(),

                    master_data.get_datapoint_22_display(),

                    master_data.get_datapoint23_display(),

                    master_data.datapoint_24,

                    master_data.datapoint_25,

                    master_data.get_datapoint26_display(),

                    master_data.get_datapoint_27_display(),

                    master_data.datapoint_28,

                    master_data.datapoint_29,

                    master_data.get_datapoint30_display(),

                    master_data.get_datapoint_31_display(),


                    master_data.get_datapoint_32_display(),

                    master_data.get_datapoint_33_display(),


                    master_data.get_datapoint_34_display(),

                    master_data.get_datapoint_35_display(),

                    master_data.get_datapoint_36_display(),

                    master_data.get_datapoint_37_display(),

                    master_data.get_datapoint_38_display(),

                    master_data.get_datapoint39_display(),

                    master_data.get_datapoint_40_display(),

                    master_data.get_datapoint_41_display(),

                    master_data.get_datapoint42_display(),

                    master_data.datapoint_43,

                    master_data.datapoint_44,

                    master_data.datapoint_45,

                    master_data.get_datapoint46_display(),
                    master_data.get_datapoint47_display(),
                    master_data.get_datapoint48_display(),
                    master_data.get_datapoint49_display(),
                    master_data.get_datapoint50_display(),

                    master_data.get_datapoint_51_display(),

                    master_data.get_datapoint_52_display(),

                    master_data.get_datapoint_53_display(),
                    master_data.get_datapoint_54_display(),


                    master_data.get_datapoint55_display(),
                    master_data.get_datapoint56_display(),
                    master_data.get_datapoint57_display(),
                    master_data.get_datapoint58_display(),
                    master_data.get_datapoint59_display(),

                    master_data.get_datapoint60_display(),

                    master_data.get_datapoint61_display(),

                    master_data.datapoint_62,

                    master_data.get_datapoint63_display(),
                    master_data.get_datapoint64_display(),

                    master_data.get_datapoint_65_display(),

                    master_data.get_datapoint66_display(),

                    master_data.get_datapoint_67_display(),

                    master_data.get_datapoint_68_display(),

                    master_data.get_datapoint69_display(),
                    master_data.get_datapoint70_display(),
                    master_data.get_datapoint71_display(),


                    master_data.get_datapoint_72_display(),
                    master_data.get_datapoint_73_display(),

                    master_data.get_datapoint74_display(),
                    master_data.get_datapoint75_display(),


                    master_data.get_datapoint76_display(),
                    master_data.get_datapoint77_display(),
                    master_data.get_datapoint78_display(),


                    master_data.get_datapoint79_display(),
                    master_data.get_datapoint80_display(),

                    master_data.get_datapoint81_display(),
                    master_data.get_datapoint82_display(),
                    master_data.get_datapoint83_display(),


                    master_data.get_datapoint_84_display(),

                    master_data.get_datapoint_85_display(),

                    master_data.get_datapoint_86_display(),

                    master_data.get_datapoint87_display(),

                    master_data.datapoint_88,

                    master_data.get_datapoint89_display(),

                    master_data.get_datapoint90_display(),

                    master_data.get_datapoint91_display(),

                    master_data.get_datapoint_92_display(),

                    master_data.get_datapoint_93_display(),

                    master_data.get_datapoint_94_display(),

                    master_data.get_datapoint95_display(),

                    master_data.datapoint_96,

                    master_data.get_datapoint97_display(),

                    master_data.get_datapoint98_display(),

                    master_data.get_datapoint_99_display(),

                    master_data.get_datapoint_100_display(),

                    master_data.get_datapoint_101_display(),

                    master_data.get_datapoint_102_display(),
                    master_data.datapoint_103,
                    master_data.get_datapoint104_display(),
                    master_data.get_datapoint105_display(),
                    master_data.get_datapoint106_display(),
                    master_data.get_datapoint107_display(),
                    master_data.get_datapoint108_display(),
                    master_data.get_datapoint109_display(),
                    master_data.get_datapoint110_display(),
                    master_data.get_datapoint111_display(),
                    master_data.get_datapoint112_display(),

                    master_data.get_datapoint113_display(),

                    master_data.get_datapoint114_display(),

                    master_data.get_datapoint115_display(),

                    master_data.get_datapoint116_display(),

                    master_data.get_datapoint117_display(),

                    master_data.get_datapoint118_display(),

                    master_data.get_datapoint119_display()

                ])

            return response

        elif format_file == 'xls':

            # content-type of response
            response = HttpResponse(content_type='application/ms-excel')

            # decide file name
            response['Content-Disposition'] = 'attachment; filename="clinical_master_table.xls"'

            # creating workbook
            wb = xlwt.Workbook(encoding='utf-8')

            # adding sheet
            ws = wb.add_sheet("sheet1")

            # Sheet header, first row
            row_num = 0

            font_style = xlwt.XFStyle()
            # headers are bold
            font_style.font.bold = True

            # column header names, you can use your own headers here
            columns = columns_names

            # write column headers in sheet
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()

            # get your data, from database or from a text file...
            for master_data in master_table:
                row_num = row_num + 1
                a = iter(range(130))

                ws.write(row_num, a.__next__(), str(master_data.create_datetime),       font_style)
                ws.write(row_num, a.__next__(), master_data.pacient.first_name,         font_style)
                ws.write(row_num, a.__next__(), master_data.pacient.last_name,          font_style)
                ws.write(row_num, a.__next__(), str(master_data.pacient.date_of_birth), font_style)
                ws.write(row_num, a.__next__(), master_data.pacient.phone,              font_style)
                ws.write(row_num, a.__next__(), master_data.pacient.nsh_id,             font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_7,                font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint8_display(),             font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_9_display(),    font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_10_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_11_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_12_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_13_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_14_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint15_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint16_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_16_b_display(), font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_16_b_display(), font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_17_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint18_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint19_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint20_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_21_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_22_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint23_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_24,               font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_25,               font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint26_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_27_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_28_display(),               font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_29_display(),               font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint30_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_31_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_32_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_33_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_34_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_35_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_36_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_37_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_38_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint39_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_40_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_41_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint42_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_43,               font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_44,               font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_45,               font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint46_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint47_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint48_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint49_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint50_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_51_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_52_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_53_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_54_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint55_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint56_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint57_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint58_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint59_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint60_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint61_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_62,               font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint63_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint64_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_65_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint66_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_67_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_68_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint69_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint70_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint71_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_72_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_73_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint74_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint75_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint76_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint77_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint78_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint79_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint80_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint81_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint82_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint83_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_84_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_85_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_86_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint87_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_88,               font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint89_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint90_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint91_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_92_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_93_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_94_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint95_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_96,               font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint97_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint98_display(),            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_99_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_100_display(),  font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_101_display(),  font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_102_display(),  font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_103,              font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint104_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint105_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint106_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint107_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint108_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint109_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint110_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint111_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint112_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint113_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint114_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint115_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint116_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint117_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint118_display(),           font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint119_display(),           font_style)


            wb.save(response)
            return response

        else:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="clinical_master_table.csv"'

            writer = csv.writer(response)
            writer.writerow(columns_names)

            for pacient_data in master_table:
                writer.writerow([
                    pacient_data.id,
                    pacient_data.nsh_id,
                    pacient_data.first_name,
                    pacient_data.last_name,
                    str(pacient_data.date_of_birth),
                    pacient_data.phone,
                    pacient_data.email,
                    pacient_data.default_city,
                    pacient_data.home_addres,

                ])

            return response
def login_view(request):
    if request.method == "POST":
        try:
            request_data = request.POST
            username = request_data.get('username')

            password = request_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/master/')
        except BaseException:
            return render(request, 'auth/login.html')

    else:
        return render(request, 'auth/login.html')

def datadictionary_view(request):
    if request.method == "GET":
        return render(request,'ddactionary/ddactionary.html')
def loadbusinessbuysale(data_):
    if data_:
        parse_id = str(uuid4())
        for company_ in data_:

            #   name = "БЕРЕЗКА ПЛЮС, ООО",

            try:
                name = str(company_['name']).strip().replace(" ", "")
            except BaseException:
                name = ""

            #  type_company = "ООО",
            try:
                type_company = str(
                    company_['type_company']).strip().replace(
                    " ", "")
            except BaseException:
                type_company = ""

            #  brand = "БЕРЕЗКА ПЛЮС",
            try:
                brand = str(company_['brand']).strip().replace(" ", "")
            except BaseException:
                brand = ""

            #  mail_company = null,
            try:
                mail_company = str(
                    company_['mail_company']).strip().replace(
                    " ", "")
            except BaseException:
                mail_company = ""

            #  inn_company = null,
            try:
                inn_company = str(
                    company_['inn_company']).strip().replace(
                    " ", "")
            except BaseException:
                inn_company = ""

            #  check_date = 02.07.2014",
            try:
                check_date = str(
                    company_['check_date']).strip().replace(
                    " ", "")
            except BaseException:
                check_date = ""

            #  manager_ceo = "Алистратов Олег Александрович",
            try:
                manager_ceo = str(
                    company_['manager_ceo']).strip().replace(
                    " ", "")
            except BaseException:
                manager_ceo = ""

            #  manager_fin = "Алистратов Олег Александрович",
            try:
                manager_fin = str(
                    company_['manager_fin']).strip().replace(
                    " ", "")
            except BaseException:
                manager_fin = ""

            #  q_employ = 6
            try:
                q_employ = str(company_['q_employ']).strip().replace(" ", "")
            except BaseException:
                q_employ = ""

            #  title = ""
            try:
                title = str(company_['title']).strip().replace(" ", "")
            except BaseException:
                title = ""

            #  site = ""
            try:
                site = str(company_['site']).strip().replace(" ", "")
            except BaseException:
                site = ""

            #  adress_fact = "83059 г. Донецк, ул. 8-го Марта, 34а"
            try:
                adress_fact = str(
                    company_['adress_fact']).strip().replace(
                    " ", "")
            except BaseException:
                adress_fact = ""

            #  adress_yure = "83059 г. Донецк, ул. 8-го Марта, 34а"
            try:
                adress_yure = str(
                    company_['adress_yure']).strip().replace(
                    " ", "")
            except BaseException:
                adress_yure = ""

            #  adress_post = ""
            try:
                adress_post = str(
                    company_['adress_post']).strip().replace(
                    " ", "")
            except BaseException:
                adress_post = ""

            #  phone_company = "380506233143"
            try:
                phone_company = str(
                    company_['phone_company']).strip().replace(
                    " ", "")
            except BaseException:
                phone_company = ""

            #  phone_company = "380506233143"
            try:
                phone_ceo = str(company_['phone_ceo']).strip().replace(" ", "")
            except BaseException:
                phone_ceo = ""

            #  phone_fin = "380506233143"
            try:
                phone_fin = str(company_['phone_fin']).strip().replace(" ", "")
            except BaseException:
                phone_fin = ""

            #  phone_fax = "380506233143"
            try:
                phone_fax = str(company_['phone_fax']).strip().replace(" ", "")
            except BaseException:
                phone_fax = ""

            #  phone_contact = "[380506233143]"
            try:
                phone_contact = company_['phone_contact']
            except BaseException:
                phone_contact = []

            #  prod_serv = "Формирование и обработка листового стекла"
            try:
                prod_serv = str(company_['prod_serv']).strip().replace(" ", "")
            except BaseException:
                prod_serv = ""

            #  webpage = "https://www.ua-region.info/35711197"
            try:
                webpage = str(company_['webpage']).strip().replace(" ", "")
            except BaseException:
                webpage = ""

            #  description = "https://www.ua-region.info/35711197"
            try:
                description = str(
                    company_['description']).strip().replace(
                    " ", "")
            except BaseException:
                description = ""

            #  company_logo = "https://www.ua-region.info/35711197"

            try:
                company_logo = str(
                    company_['company_logo']).strip().replace(
                    " ", "")
            except BaseException:
                company_logo = None

            #  person_slug = "dsfgsdfexawe"

            try:
                person_slug = str(
                    company_['person_slug']).strip().replace(
                    " ", "")
            except BaseException:
                person_slug = None

            #  source = ""

            try:
                source = str(company_['source']).strip().replace(" ", "")
            except BaseException:
                source = ""

            #  source = list
            try:
                activities = company_['activities']
            except BaseException:
                activities = []

            #  industry = list
            try:
                industry = company_['industry']
            except BaseException:
                industry = []

            businessBuySale_ = BusinessBuySale.objects.create(
                person_slug=person_slug,
                brand=brand,
                title=title,
                offname=name,
                type=type_company,
                type_company=type_company,
                descrition=description,
                prod_serv=prod_serv,
                webpage=webpage,
                company_logo=company_logo,
                source=source,
                adress_yure=adress_yure,
                adress_fact=adress_fact,
                adress_post=adress_post,
                mail_company=mail_company,
                mail_ceo="",
                mail_contact="",
                mail_info="",
                mail_is_find=False,
                mail_is_send=False,
                mail_is_recived=False,
                site_is_work=False,
                disscus_mail="",
                disscus_phone="",
                disscus_name="",
                disscus_status="",
                manager_ceo=manager_ceo,
                manager_fin=manager_fin,
                mail_link="",
                unique_id=parse_id,
                phone_company=phone_company,
                phone_contact=phone_contact,
                phone_ceo=phone_ceo,
                phone_fin=phone_fin,
                phone_fax=phone_fax,
                q_employ=q_employ,
                inn_company=inn_company,
                site=site)
            businessBuySale_.set_phone_contact(phone_contact)
            businessBuySale_.set_activities(activities)
            businessBuySale_.set_industries(industry)
            businessBuySale_.save()

def procces_pacient(record_list):
    first_name = record_list[1]
    last_name = record_list[2]
    date_of_birth = record_list[3]
    phone = record_list[4]
    email = record_list[7]
    email = email if vaidator_data.validate_email(email) else ""



    date_of_birth = vaidator_data.validate_date(date_of_birth)
    date_of_birth = date_of_birth if date_of_birth else None
    if first_name and last_name:

        pacient, created = Pacient.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,

        )
    else: return None

    if created:
        try:
            nsh_id_old = Pacient.objects.all().order_by('-id')[1]
            nsh_id_old = str(nsh_id_old.nsh_id)

            nsh_id_new = gen_aaaannnna(nsh_id_old)
        except:
            nsh_id_new = gen_aaaannnna()

        pacient.nsh_id = nsh_id_new
    pacient_id = pacient.id

    pacient.phone = phone
    pacient.email = email

    pacient.save()

    return pacient_id

def parse_datapoint_52(data):
    return_data = []
    datas = data.split('\n')
    for n,data_ in enumerate(datas):
        r = data_.split('[]:')[-1].split("months:")[-1].strip()
        return_data.append([n+1,r])

    return return_data

def parse_operation(data):
    return_data = []
    datas = data.split('\n')
    for data_ in datas:
        r = data_.split(",")
        r = [r_i.split(":")[-1].strip() for r_i in r]


        return_data.append(r)




    return return_data


def parse_datapoint_62(data,size=0):
    return_data = []
    datas = data.split('\n')

    for data_ in datas:
        r = data_.split(",")
        r2 = [r_i.split(":")[-1].strip() for r_i in r]
        if size != 0 and len(r2) > size:
            try:
                rl = []
                for i in range(1, int(len(r2) / int(size) + 1)):
                    r_l = r2[(i - 1) * size:i * size]
                    return_data.append(r_l)
            except:

                r_l.append(len(size-r_l)*"")

        else:
            return_data.append(r2)

    return return_data

def data_dictionatyDelete(request,req_id):
    if request.method == "POST":
        ddict = DataDictionary.objects.get(id=req_id)
        ddict.is_hide = True
        ddict.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def data_dictionaty(request):
    if request.method == "GET":
        search_param = {'is_hide':False}
        page = 1
        data_dictionary = DataDictionary.objects.filter(**search_param).order_by('id')[(page - 1) * 50:50 * page]
        return render(request,'ddactionary/ddactionary.html',{"data_dictionary":data_dictionary})

    elif request.method=="POST":
        print(request.POST)

        f_code = request.POST.get('f_code')
        f_score = request.POST.get('f_score')

        f_score_a = request.POST.get('f_score_a')

        f_score_b = request.POST.get('f_score_b')

        data_points = request.POST.get('data_points')

        value = request.POST.get('data_dictionary')

        display_destination = request.POST.get('display_destination')

        u_score = request.POST.get('u_score')

        link_logic = request.POST.get('link_logic')
        if link_logic == "Yes":
            link_logic = True
        else:
            link_logic = False

        color_spect = request.POST.get('color_spect')


        data_dictionary_= DataDictionary.objects.create(
                        color=color_spect,
                        link_logic=link_logic,
                        u_score=u_score,
                        display_distenation=display_destination,
                        data_point=data_points,
                        value=value,
                        f_score_b=f_score_b,
                        f_score_a=f_score_a,
                        f_score=f_score,f_code=f_code
                    )

        data_dictionary_.save()


        return redirect('/datadictionary/')
def parse_drugs(data):
    return_data = []
    l = re.split(r"(\: \d\,)* unique\:\d\[\]\:", data.replace('\n', ' '))

    for i in l:
        if i:
            prep = i.replace(":", "").replace(",", "").strip()
            if prep and len(prep) >= 3:
                return_data.append(prep)


    if not return_data:
        drugs = Drug.objects.all().values('name')
        for drug_name in drugs:
            if str(drug_name) in str(data):
                return_data.append(drug_name)



    return return_data

def master_table_view(request):
    if request.method == "GET":


        search_param = {}

        page = request.GET.get('page') if request.GET.get('page') else 1
        page = int(page)

        first_name = request.GET.get('first_name')

        last_name = request.GET.get('last_name')

        phone = request.GET.get('phone')

        email = request.GET.get('email')

        nsh_id = request.GET.get('nsh_id')

        default_city = request.GET.get('city')

        home_addres = request.GET.get('addres')
        birth_from = request.GET.get('birth_from')

        birth_to = request.GET.get('birth_to')
        search_param['is_hide'] = False
        if email:
            email = vaidator_data.validate_email(str(email))

            search_param['pacient__email'] = email

        if nsh_id:
            nsh_id = str(nsh_id)

            search_param['pacient__nsh_id'] = nsh_id

        if first_name:

            search_param['pacient__first_name'] = first_name

        if last_name:

            search_param['pacient__last_name'] = last_name

        if phone:
            phone = vaidator_data.validate_phone(str(phone))

            search_param['pacient__phone'] = phone

        if default_city:
            default_city = str(default_city)

            search_param['pacient__default_city'] = default_city

        if home_addres:
            home_addres = str(home_addres)

            search_param['pacient__home_addres'] = home_addres


        master_table = DataFormTable.objects.filter(**search_param).order_by('create_datetime')[(page-1)*50:50*page]
        return render(request,'masterTable/masterTable.html',{
            'master_table':master_table,'user':request.user,
        })

    if request.method == "POST":
        try:
            file_ProfileForm = request.FILES['file_ProfileForm']
            file_ProfileForm = file_ProfileForm if file_ProfileForm else None
        except:
            file_ProfileForm = None


        try:

            file_DataForm = request.FILES['file_DataForm']
            print(file_DataForm)
            file_DataForm = file_DataForm if file_DataForm else None
            print(file_DataForm)

            dfs = pd.read_excel(file_DataForm)
            print(dfs)
            # from pyexcel_xls import get_data as xls_get
            # from pyexcel_xlsx import get_data as xlsx_get

            # file_DataForm = request.FILES['file_DataForm']
            # pd.read_excel(file_DataForm, )
            # print("file_DataForm",file_DataForm)
            # if (str(file_DataForm).split('.')[-1] == 'xls'):
            #     data = xls_get(file_DataForm, column_limit=120)
            #     print("data", data)
            # elif (str(file_DataForm).split('.')[-1] == 'xlsx'):
            #     data = xlsx_get(file_DataForm, column_limit=120)
            #     print("data", data)
            for i in dfs:
                print(i)
        except:
            file_DataForm = None

        google_drive_url_ProfileForm = request.POST.get('google_drive_url_ProfileForm')
        google_drive_url_ProfileForm = google_drive_url_ProfileForm if google_drive_url_ProfileForm else None

        google_drive_url_DataForm = request.POST.get('google_drive_url_DataForm')
        google_drive_url_DataForm = google_drive_url_DataForm if google_drive_url_DataForm else None

        if google_drive_url_DataForm:

            gg_drive_proccess1 = GoogleDrive(google_drive_url_DataForm)
            gg_drive_proccess1.request()
            gg_drive_proccess1.gog_drive_to_json()
            gg_drive_proccess1.data_from_jjson()
            for row_ in gg_drive_proccess1.table_data:
                pacient_id = procces_pacient(row_[:8])


                if pacient_id ==  None: continue

                create_datetime = vaidator_data.validate_datetime(row_[0])

                try:
                    profile_form = ProfileFormTable.objects.filter(
                        pacient_id=pacient_id,
                    ).order_by("-create_datetime")[0]
                except:
                    profile_form = ProfileFormTable.objects.create(pacient_id=pacient_id)
                    profile_form.save()

                try:
                    nsh_id_gdisk = row_[120]

                    data_form, created = DataFormTable.objects.get_or_create(
                        nsh_id_gdisk=nsh_id_gdisk
                    )
                except:
                    data_form, created = DataFormTable.objects.get_or_create(
                        pacient_id=pacient_id,
                        create_datetime=create_datetime,
                        profile_data_id=profile_form.id


                    )
                if data_form:

                    data_form.datapoint_7 = row_[6]
                    data_form.datapoint_8 = row_[7]
                    data_form.datapoint_9 = row_[8]
                    data_form.datapoint_10 = row_[9]


                    datapoint_11 = row_[10]
                    data_form.datapoint_11 = datapoint_11
                    data_form.datapoint_12 = row_[11]
                    data_form.datapoint_13 = row_[12]
                    data_form.datapoint_14 = row_[13]
                    data_form.datapoint_15 = row_[14]
                    data_form.datapoint_16 = row_[15]

                    data_form.datapoint_16a = row_[16]
                    data_form.datapoint_16b = row_[17]
                    data_form.datapoint_17 = row_[18]
                    data_form.datapoint_18 = row_[19]
                    data_form.datapoint_19 = row_[20]

                    data_form.datapoint_20 = row_[21]
                    data_form.datapoint_21 = row_[22]
                    data_form.datapoint_22 = row_[23]
                    data_form.datapoint_23 = row_[24]
                    data_form.datapoint_24 = row_[25]
                    data_form.datapoint_25 = row_[26]
                    data_form.datapoint_26 = row_[27]
                    data_form.datapoint_27 = row_[28]
                    data_form.datapoint_28 = row_[29]


                    data_form.datapoint_30 = row_[30]
                    data_form.datapoint_31 = row_[31]
                    data_form.datapoint_32 = row_[32]
                    data_form.datapoint_33 = row_[33]
                    data_form.datapoint_34 = row_[34]
                    data_form.datapoint_35 = row_[35]
                    data_form.datapoint_36 = row_[36]
                    data_form.datapoint_37 = row_[37]
                    data_form.datapoint_38 = row_[38]
                    data_form.datapoint_39 = row_[39]


                    data_form.datapoint_40 = row_[40]
                    data_form.datapoint_41 = row_[41]
                    data_form.datapoint_42 = row_[42]
                    data_form.datapoint_43 = row_[43]
                    data_form.datapoint_44 = row_[44]
                    data_form.datapoint_45 = row_[45]
                    data_form.datapoint_46 = row_[46]
                    data_form.datapoint_47 = row_[47]
                    data_form.datapoint_48 = row_[48]
                    data_form.datapoint_49 = row_[49]


                    data_form.datapoint_50 = row_[50]
                    data_form.datapoint_51 = row_[51]
                    data_form.datapoint_52 = row_[52]
                    data_form.datapoint_53 = row_[53]
                    data_form.datapoint_54 = row_[54]
                    data_form.datapoint_55 = row_[55]
                    data_form.datapoint_56 = row_[56]
                    data_form.datapoint_57 = row_[57]
                    data_form.datapoint_58 = row_[58]
                    data_form.datapoint_59 = row_[59]


                    data_form.datapoint_60 = row_[60]
                    data_form.datapoint_61 = row_[61]
                    data_form.datapoint_62 = row_[62]
                    data_form.datapoint_63 = row_[63]
                    data_form.datapoint_64 = row_[64]
                    data_form.datapoint_65 = row_[65]
                    data_form.datapoint_66 = row_[66]
                    data_form.datapoint_67 = row_[67]
                    data_form.datapoint_68 = row_[68]
                    data_form.datapoint_69 = row_[69]


                    data_form.datapoint_70 = row_[70]
                    data_form.datapoint_71 = row_[71]
                    data_form.datapoint_72 = row_[72]
                    data_form.datapoint_73 = row_[73]
                    data_form.datapoint_74 = row_[74]
                    data_form.datapoint_75 = row_[75]
                    data_form.datapoint_76 = row_[76]
                    data_form.datapoint_77 = row_[77]
                    data_form.datapoint_78 = row_[78]
                    data_form.datapoint_79 = row_[79]


                    data_form.datapoint_80 = row_[80]
                    data_form.datapoint_81 = row_[81]
                    data_form.datapoint_82 = row_[82]
                    data_form.datapoint_83 = row_[83]
                    data_form.datapoint_84 = row_[84]
                    data_form.datapoint_85 = row_[85]
                    data_form.datapoint_86 = row_[86]
                    data_form.datapoint_87 = row_[87]
                    data_form.datapoint_88 = row_[88]
                    data_form.datapoint_89 = row_[89]


                    data_form.datapoint_90 = row_[90]
                    data_form.datapoint_91 = row_[91]
                    data_form.datapoint_92 = row_[92]
                    data_form.datapoint_93 = row_[93]
                    data_form.datapoint_94 = row_[94]
                    data_form.datapoint_95 = row_[95]
                    data_form.datapoint_96 = row_[96]
                    data_form.datapoint_97 = row_[97]
                    data_form.datapoint_98 = row_[98]
                    data_form.datapoint_99 = row_[99]


                    data_form.datapoint_100 = row_[100]
                    data_form.datapoint_101 = row_[101]
                    data_form.datapoint_102 = row_[102]
                    data_form.datapoint_103 = row_[103]
                    data_form.datapoint_104 = row_[104]
                    data_form.datapoint_105 = row_[105]
                    data_form.datapoint_106 = row_[106]
                    data_form.datapoint_107 = row_[107]
                    data_form.datapoint_108 = row_[108]
                    data_form.datapoint_109 = row_[109]


                    data_form.datapoint_110 = row_[110]
                    data_form.datapoint_111 = row_[111]
                    data_form.datapoint_112 = row_[112]
                    data_form.datapoint_113 = row_[113]
                    data_form.datapoint_114 = row_[114]
                    data_form.datapoint_115 = row_[115]
                    data_form.datapoint_116 = row_[116]
                    data_form.datapoint_117 = row_[117]
                    data_form.datapoint_118 = row_[118]
                    data_form.datapoint_119 = row_[119]


                    data_form.datapoint_120 = row_[120]





                    data_form.save()



        if google_drive_url_ProfileForm:

            gg_drive_proccess2 = GoogleDrive(google_drive_url_ProfileForm)
            gg_drive_proccess2.request()
            gg_drive_proccess2.gog_drive_to_json()
            gg_drive_proccess2.data_from_jjson()

            for row_ in gg_drive_proccess2.table_data:
                pacient_id = procces_pacient(row_[:8])
                if pacient_id == None: continue
                else:

                    create_datetime = vaidator_data.validate_datetime(row_[0])


                    try:
                        nsh_id_gdisk = row_[96]
                        profile_form, created = ProfileFormTable.objects.get_or_create(
                            nsh_id_gdisk=nsh_id_gdisk
                        )
                    except:
                        profile_form, created = ProfileFormTable.objects.get_or_create(
                            pacient_id=pacient_id,
                            create_datetime=create_datetime)


                    if profile_form:
                        profile_form.sex = row_[8]
                        profile_form.datapoint_10 = row_[9]

                        metic_sys = row_[10]
                        profile_form.metic_sys = metic_sys

                        profile_form.datapoint_12 = row_[11]
                        profile_form.datapoint_13a = row_[12]
                        profile_form.datapoint_13b = row_[13]
                        profile_form.datapoint_14 = row_[14]
                        profile_form.datapoint_15 = row_[15]
                        profile_form.datapoint_16 = row_[16]
                        profile_form.datapoint_17 = row_[17]
                        profile_form.datapoint_18 = row_[18]
                        profile_form.datapoint_19 = row_[19]
                        profile_form.datapoint_20 = row_[20]
                        profile_form.datapoint_21 = row_[21]
                        profile_form.datapoint_22 = row_[22]
                        profile_form.datapoint_23 = row_[23]
                        profile_form.datapoint_24 = row_[24]
                        profile_form.datapoint_25 = row_[25]
                        profile_form.datapoint_26 = row_[26]
                        profile_form.datapoint_27 = row_[27]
                        profile_form.datapoint_28 = row_[28]

                        datapoint_29 = row_[29]
                        if datapoint_29:
                            datapoint_29_list_id = []
                            datapoint_29_list = parse_drugs(datapoint_29)
                            if datapoint_29_list:
                                for datapoint_29_name in datapoint_29_list:
                                    drug,created_dr1 = Drug.objects.get_or_create(name=datapoint_29_name)
                                    if created_dr1:
                                        drug.save()
                                    datapoint_29_list_id.append(drug)
                            profile_form.datapoint_29.add(*datapoint_29_list_id)

                        datapoint_30 = row_[30]
                        if datapoint_30:
                            datapoint_30_list_id = []
                            datapoint_30_list = parse_drugs(datapoint_30)
                            if datapoint_30_list:
                                for datapoint_30_name in datapoint_30_list:
                                    drug1, created_dr2 = Drug.objects.get_or_create(name=datapoint_30_name)
                                    if created_dr2:
                                        drug1.save()
                                    datapoint_30_list_id.append(drug1)

                            profile_form.datapoint_30.add(*datapoint_30_list_id)

                        datapoint_31 = row_[31]

                        if datapoint_31:
                            datapoint_31_list_id = []
                            datapoint_31_list = parse_operation(datapoint_31)
                            if datapoint_31_list:
                                for n,datapoint_31_vars in enumerate(datapoint_31_list):
                                    operation, created_op = MedicalOperation.objects.get_or_create(
                                        title=datapoint_31_vars[1],
                                        date_operation=vaidator_data.validate_date(datapoint_31_vars[2]),
                                        num_operation=datapoint_31_vars[0]
                                        )
                                    if created_op:
                                        operation.save()
                                    datapoint_31_list_id.append(operation)

                            profile_form.datapoint_31.add(*datapoint_31_list_id)


                        profile_form.datapoint_32 = row_[32]

                        datapoint_33 = row_[33]
                        datapoint_33 = vaidator_data.validate_date(datapoint_33) if vaidator_data.validate_date(datapoint_33) else None
                        profile_form.datapoint_33 = datapoint_33
                        profile_form.datapoint_34 = row_[34]
                        profile_form.datapoint_35 = row_[35]
                        profile_form.datapoint_36 = row_[36]
                        profile_form.datapoint_37 = row_[37]
                        profile_form.datapoint_38 = row_[38]
                        profile_form.datapoint_39 = row_[39]

                        profile_form.datapoint_40 = row_[40]
                        profile_form.datapoint_41 = row_[41]
                        profile_form.datapoint_42 = row_[42]
                        profile_form.datapoint_43 = row_[43]
                        profile_form.datapoint_44 = row_[44]
                        profile_form.datapoint_45 = row_[45]
                        profile_form.datapoint_46 = row_[46]
                        profile_form.datapoint_47 = row_[47]
                        profile_form.datapoint_48 = row_[48]
                        profile_form.datapoint_49 = row_[49]

                        profile_form.datapoint_50 = row_[50]
                        profile_form.datapoint_51 = row_[51]


                        datapoint_52 = row_[52]

                        if datapoint_52:
                            datapoint_52_list_id = []
                            datapoint_52_list = parse_datapoint_52(datapoint_52)
                            if datapoint_52_list:
                                for n,datapoint_52_vars in enumerate(datapoint_52_list):
                                    chldPacientDurBreast, created_chld = ChldPacientDurBreast.objects.get_or_create(
                                        num_child=int(datapoint_52_vars[0]),
                                        period_months=int(datapoint_52_vars[1]),
                                        )
                                    if created_chld:
                                        chldPacientDurBreast.save()
                                    datapoint_52_list_id.append(chldPacientDurBreast)

                            profile_form.datapoint_52.add(*datapoint_52_list_id)



                        profile_form.datapoint_53 = row_[53]
                        profile_form.datapoint_54 = row_[54]
                        profile_form.datapoint_55 = row_[55]
                        profile_form.datapoint_56 = row_[56]
                        profile_form.datapoint_57 = row_[57]
                        profile_form.datapoint_58 = row_[58]
                        profile_form.datapoint_59 = row_[59]

                        profile_form.datapoint_60 = row_[60]
                        profile_form.datapoint_61 = row_[61]

                        datapoint_62 = row_[62]
                        if datapoint_62:
                            datapoint_62_list_id = []
                            datapoint_62_list = parse_datapoint_62(datapoint_62,4)
                            if datapoint_62_list:
                                for n,datapoint_62_vars in enumerate(datapoint_62_list):
                                    cancer_,cancer_new = Cancer.objects.get_or_create(title=datapoint_62_vars[1])
                                    chldPacientDurBreast, created_chld = RelationhipPacient.objects.get_or_create(
                                        type_cancer=cancer_,
                                        relation=datapoint_62_vars[0],
                                        age_diagnise=int(datapoint_62_vars[2]),
                                        position_cancer=datapoint_62_vars[3]
                                        )
                                    if created_chld:
                                        chldPacientDurBreast.save()
                                    datapoint_62_list_id.append(chldPacientDurBreast)

                            profile_form.datapoint_62.add(*datapoint_62_list_id)



                        profile_form.datapoint_63 = row_[63]

                        datapoint_64 = row_[64]
                        if datapoint_64:
                            datapoint_64_list_id = []
                            datapoint_64_list = parse_datapoint_62(datapoint_64,3)
                            if datapoint_64_list:
                                for n, datapoint_64_vars in enumerate(datapoint_64_list):

                                    cancer,cr_cancer = Cancer.objects.get_or_create(title=datapoint_64_vars[1])
                                    chldPacientDurBreast, created_chld = RelationhipPacient.objects.get_or_create(
                                        type_cancer=cancer,
                                        relation=datapoint_64_vars[0],
                                        age_diagnise=int(datapoint_64_vars[2]),
                                    )
                                    if created_chld:
                                        chldPacientDurBreast.save()
                                    datapoint_64_list_id.append(chldPacientDurBreast)

                            profile_form.datapoint_64.add(*datapoint_64_list_id)


                        profile_form.datapoint_65 = row_[65]

                        datapoint_66 = row_[66]
                        if datapoint_66:
                            datapoint_66_list_id = []
                            datapoint_66_list = parse_datapoint_62(datapoint_66)
                            if datapoint_66_list:
                                for n, datapoint_66_vars in enumerate(datapoint_66_list):

                                    cancer,create_cancer = Cancer.objects.get_or_create(title=datapoint_66_vars[1])
                                    cancer_h, create_cancer_h = CancerHistory.objects.get_or_create(
                                        cancer=cancer,
                                        date_detect=vaidator_data.validate_date(datapoint_66_vars[2])
                                    )

                                    if create_cancer_h:
                                        cancer_h.save()
                                    datapoint_66_list_id.append(cancer_h)

                            profile_form.datapoint_66.add(*datapoint_66_list_id)


                        profile_form.datapoint_67 = row_[67]
                        profile_form.datapoint_68 = row_[68]
                        profile_form.datapoint_69 = row_[69]

                        profile_form.datapoint_70 = row_[70]
                        profile_form.datapoint_71 = row_[71]
                        profile_form.datapoint_72 = row_[72]
                        profile_form.datapoint_73 = row_[73]
                        profile_form.datapoint_74 = row_[74]
                        profile_form.datapoint_75 = row_[75]
                        profile_form.datapoint_76 = row_[76]
                        profile_form.datapoint_77 = row_[77]
                        profile_form.atapoint_78 = row_[78]
                        profile_form.datapoint_79 = row_[79]

                        profile_form.datapoint_80 = row_[80]
                        profile_form.datapoint_81 = row_[81]
                        profile_form.datapoint_82 = row_[82]
                        profile_form.datapoint_83 = row_[83]
                        profile_form.datapoint_84 = row_[84]
                        profile_form.datapoint_85 = row_[85]
                        profile_form.datapoint_86 = row_[86]
                        profile_form.datapoint_87 = row_[87]
                        profile_form.datapoint_88 = row_[88]
                        profile_form.datapoint_89 = row_[89]

                        profile_form.datapoint_90 = row_[90]
                        profile_form.datapoint_91 = row_[91]
                        profile_form.datapoint_92 = row_[92]
                        profile_form.datapoint_93 = row_[93]
                        profile_form.datapoint_94 = row_[94]
                        profile_form.datapoint_95 = row_[95]
                        try:
                            profile_form.nsh_id_gdisk = row_[96]
                        except:
                            print("err", row_[93:])
                    profile_form.save()
                    try:
                        data_form = DataFormTable.objects.filter(
                            pacient_id=pacient_id,
                            profile_data=profile_form,
                        ).order_by('-create_datetime')[0]
                    except:
                        data_form = DataFormTable.objects.create(
                            pacient_id=pacient_id,
                            profile_data=profile_form,
                            create_datetime=create_datetime
                        )
                    data_form.save()






        return render(request, 'desctop/succsespage/suucsespage.html')



def pacientDelete(request,req_id):
    if request.method == "POST":
        pacient = Pacient.objects.get(id=req_id)
        pacient.is_hide = True
        pacient.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def masterTableDelete(request,req_id):
    if request.method == "POST":
        mastab = DataFormTable.objects.get(id=req_id)
        mastab.is_hide = True
        mastab.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def pacientDownloadFile(request):
    if request.method =='GET':
        format_file = request.GET.get('format_file')

        format_file = format_file if format_file else 'csv'

        search_param = {}

        first_name = request.GET.get('first_name')

        last_name = request.GET.get('last_name')

        phone = request.GET.get('phone')

        email = request.GET.get('email')

        nsh_id = request.GET.get('nsh_id')

        default_city = request.GET.get('city')

        home_addres = request.GET.get('addres')
        birth_from = request.GET.get('birth_from')

        birth_to = request.GET.get('birth_to')

        if email:
            email = vaidator_data.validate_email(str(email))

            search_param['email'] = email

        if nsh_id:
            nsh_id = str(nsh_id)

            search_param['nsh_id'] = nsh_id

        if first_name:

            search_param['first_name'] = first_name

        if last_name:

            search_param['last_name'] = last_name

        if phone:
            phone = vaidator_data.validate_phone(str(phone))

            search_param['phone'] = phone

        if default_city:
            default_city = str(default_city)

            search_param['default_city'] = default_city

        if home_addres:
            home_addres = str(home_addres)

            search_param['home_addres'] = home_addres
        search_param['is_hide'] = False
        # if birth_from and birth_to:
        #     birth_from = vaidator_data.validate_date(str(birth_from))
        #
        #     search_param['date_of_birth__range'] = [birth_from, birth_to]
        #
        # elif birth_from:
        #     birth_from = vaidator_data.validate_date(str(birth_from))
        #
        #     search_param['date_of_birth__range'] = [birth_from, '2023-12-30']
        #
        # elif birth_to:
        #     birth_to = vaidator_data.validate_date(str(birth_to))
        #
        #     search_param['date_of_birth__range'] = ['1900-01-01',birth_to]
        #
        # else:
        #     search_param['date_of_birth__range'] = ['1900-01-01','2023-12-30']

        pacients = Pacient.objects.filter(
            **search_param
        ).order_by('-id')

        columns_names = ['ID', 'NSH ID', 'First Name', 'Last Name', 'Date of birth',
                         'Pacient phone', 'Email', 'City', 'Address']

        if format_file == 'csv':



            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="clinical_pacients.csv"'

            writer = csv.writer(response)
            writer.writerow(columns_names)

            for pacient_data in pacients:
                writer.writerow([
                    pacient_data.id,
                    pacient_data.nsh_id,
                    pacient_data.first_name,
                    pacient_data.last_name,
                    str(pacient_data.date_of_birth),
                    pacient_data.phone,
                    pacient_data.email,
                    pacient_data.default_city,
                    pacient_data.home_addres,


                                 ])

            return response

        elif format_file == 'xls':

            # content-type of response
            response = HttpResponse(content_type='application/ms-excel')

            # decide file name
            response['Content-Disposition'] = 'attachment; filename="clicin_pacient.xls"'

            # creating workbook
            wb = xlwt.Workbook(encoding='utf-8')

            # adding sheet
            ws = wb.add_sheet("sheet1")

            # Sheet header, first row
            row_num = 0

            font_style = xlwt.XFStyle()
            # headers are bold
            font_style.font.bold = True

            # column header names, you can use your own headers here
            columns = columns_names

            # write column headers in sheet
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)

            # Sheet body, remaining rows
            font_style = xlwt.XFStyle()

            # get your data, from database or from a text file...
            for pacient in pacients:
                row_num = row_num + 1

                ws.write(row_num, 0, pacient.id, font_style)
                ws.write(row_num, 1, pacient.nsh_id, font_style)
                ws.write(row_num, 2, pacient.first_name, font_style)
                ws.write(row_num, 3, pacient.last_name, font_style)
                ws.write(row_num, 4, str(pacient.date_of_birth), font_style)
                ws.write(row_num, 5, pacient.phone, font_style)
                ws.write(row_num, 6, pacient.email, font_style)
                ws.write(row_num, 7, pacient.default_city, font_style)
                ws.write(row_num, 8, pacient.home_addres, font_style)

            wb.save(response)
            return response

        else:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="clinical_pacients.csv"'

            writer = csv.writer(response)
            writer.writerow(columns_names)

            for pacient_data in pacients:
                writer.writerow([
                    pacient_data.id,
                    pacient_data.nsh_id,
                    pacient_data.first_name,
                    pacient_data.last_name,
                    str(pacient_data.date_of_birth),
                    pacient_data.phone,
                    pacient_data.email,
                    pacient_data.default_city,
                    pacient_data.home_addres,

                ])

            return response

def pacientLoad(request):
    if request.method == "POST":
        fileuploadInput = request.FILES['fileuploadInput']

        linkGD = request.POST.get('linkGD')

        gd = GoogleDrive(linkGD)
        gd.request()
        gd.data_from_jjson()



def pacientsView(request):
    if request.method=="POST":

        first_name = request.POST.get('first_name')

        last_name = request.POST.get('last_name')

        phone = request.POST.get('phone')

        email = request.POST.get('email')

        nsh_id = request.POST.get('nsh_id')

        default_city = request.POST.get('city')

        home_addres = request.POST.get('addres')
        date_of_birth = request.POST.get('date_of_birth')

        try:
            nsh_id_old = Pacient.objects.all().order_by('-id')[0]
            nsh_id_old = str(nsh_id_old.nsh_id)

            nsh_id_new = gen_aaaannnna(nsh_id_old)
        except:
            nsh_id_new = gen_aaaannnna()



        if email:

            email = vaidator_data.validate_email(str(email))
        else:
            email = ''


        if first_name:
            first_name = vaidator_data.validate_firstname(str(first_name))

        else:
            first_name = ""

        if last_name:
            last_name = vaidator_data.validate_firstname(str(last_name))
        else:
            last_name = ""

        if phone:
            phone = vaidator_data.validate_phone(str(phone))

        else:
            phone = ""

        if default_city:

            default_city = str(default_city)
        else:
            default_city = ''



        if home_addres:

            home_addres = str(home_addres)
        else:
            home_addres = ""

        new_pacient = Pacient.objects.create(
                        email=email,
                        phone=phone,
                        first_name=first_name,
                        last_name=last_name,
                        default_city=default_city,
                        home_addres=home_addres,
                        date_of_birth=date_of_birth
                    )

        new_pacient.nsh_id = nsh_id_new
        new_pacient.save()


        return redirect('/pacients/')


    elif request.method=="GET":

        search_param = {}

        first_name = request.GET.get('first_name')

        last_name = request.GET.get('last_name')

        phone = request.GET.get('phone')

        email = request.GET.get('email')

        nsh_id = request.GET.get('nsh_id')

        default_city = request.GET.get('city')

        home_addres = request.GET.get('addres')
        birth_from = request.GET.get('birth_from')

        birth_to = request.GET.get('birth_to')



        if email:

            email = vaidator_data.validate_email(str(email))

            search_param['email'] = email



        search_param['is_hide'] = False

        if nsh_id:
            nsh_id = str(nsh_id)

            search_param['nsh_id'] = nsh_id

        if first_name:

            search_param['first_name'] = str(first_name)

        if last_name:
            search_param['last_name'] = str(last_name)

        if phone:
            phone = vaidator_data.validate_phone(str(phone))

            search_param['phone'] = phone

        if default_city:

            default_city = str(default_city)

            search_param['default_city'] = default_city

        if home_addres:

            home_addres = str(home_addres)

            search_param['home_addres'] = home_addres

        # if birth_from and birth_to:
        #     birth_from = vaidator_data.validate_date(str(birth_from))
        #
        #     search_param['date_of_birth__range'] = [birth_from, birth_to]
        #
        # elif birth_from:
        #     birth_from = vaidator_data.validate_date(str(birth_from))
        #
        #     search_param['date_of_birth__range'] = [birth_from, '2023-12-30']
        #
        # elif birth_to:
        #     birth_to = vaidator_data.validate_date(str(birth_to))
        #
        #     search_param['date_of_birth__range'] = ['1900-01-01',birth_to]
        #
        # else:
        #     search_param['date_of_birth__range'] = ['1900-01-01','2023-12-30']


        pacients = Pacient.objects.filter(
                        **search_param
                    ).order_by('-id')

        return render(request, 'pacients/pacients.html', {
            'pacients': pacients,
            'res_params':str(request.get_full_path())
                      .replace('/pacients/?','').replace('/pacients/','')
        })



def register_view(request):
    if request.method == "POST":
        email_ = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        phone = request.POST.get('phone')
        role = request.POST.get('role')


        if phone:
            phone = str(phone).replace('+', "")\
                .replace(' ', "").replace('(', "").replace(')', "")\
                .replace('-', "").replace('.', "")


        password = request.POST.get('password')
        repeatpassword = request.POST.get('repeatpassword')

        if password == repeatpassword:

            user_ = User.objects.create_user(
                email=email_,
                username=username,

                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user_.save()

            profile, created = UserProfile.objects.get_or_create(
                user=user_, phone=phone,role=role)
            profile.save()





            user = authenticate(username=username, password=password)
            login(request, user)
        return redirect('/master/')

    elif request.method == "GET":
        return render(request, 'auth/sign_up.html')