import csv

import xlwt
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.http import HttpResponse
from requests import Response
from rest_framework.decorators import api_view

from .models import (
    MasterTable,
    Pacient,
    gen_aaaannnna,
    UserProfile,
    User,
)
import jbssys.validators as vaidator_data


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
            first_name = vaidator_data.validate_firstname(str(first_name))

            search_param['first_name'] = first_name

        if last_name:
            print(last_name)
            last_name = vaidator_data.validate_firstname(str(last_name))
            print(last_name)
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
        master_table = MasterTable.objects.filter(**search_param).order_by('id')


        columns_names = ['Create', 'First Name', 'Surname', 'Date of birth', 'Client phone',
                         'NHS ID', 'Screener', 'Datapoint 8', 'Datapoint 9', 'Datapoint 10',
                         'Datapoint 11', 'Datapoint 12', 'Datapoint 13', 'Datapoint 14', 'Datapoint 15',
                         'Datapoint 16', 'Datapoint 16A','Datapoint 16B', 'Datapoint 17', 'Datapoint 18', 'Datapoint 19', 'Datapoint 20',
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



                    master_data.is_datapoint_8,


                    master_data.get_datapoint_9_display(),

                    master_data.get_datapoint_10_display(),

                    master_data.get_datapoint_11_display(),

                    master_data.get_datapoint_12_display(),


                    master_data.get_datapoint_13_display(),

                    master_data.get_datapoint_14_display(),

                    master_data.is_datapoint_15,

                    master_data.is_datapoint_16,

                    master_data.get_datapoint_16_b_display(),

                    master_data.get_datapoint_16_b_display(),


                    master_data.get_datapoint_17_display(),

                    master_data.is_datapoint_18,
                    master_data.is_datapoint_19,

                    master_data.is_datapoint_20,


                    master_data.get_datapoint_21_display(),

                    master_data.get_datapoint_22_display(),

                    master_data.is_datapoint_23,

                    master_data.datapoint_24,

                    master_data.datapoint_25,

                    master_data.is_datapoint_26,

                    master_data.get_datapoint_27_display(),

                    master_data.datapoint_28,

                    master_data.datapoint_29,

                    master_data.is_datapoint_30,

                    master_data.get_datapoint_31_display(),


                    master_data.get_datapoint_32_display(),

                    master_data.get_datapoint_33_display(),


                    master_data.get_datapoint_34_display(),

                    master_data.get_datapoint_35_display(),

                    master_data.get_datapoint_36_display(),

                    master_data.get_datapoint_37_display(),

                    master_data.get_datapoint_38_display(),

                    master_data.is_datapoint_39,

                    master_data.get_datapoint_40_display(),

                    master_data.get_datapoint_41_display(),

                    master_data.is_datapoint_42,

                    master_data.datapoint_43,

                    master_data.datapoint_44,

                    master_data.datapoint_45,

                    master_data.is_datapoint_46,
                    master_data.is_datapoint_47,
                    master_data.is_datapoint_48,
                    master_data.is_datapoint_49,
                    master_data.is_datapoint_50,

                    master_data.get_datapoint_51_display(),

                    master_data.get_datapoint_52_display(),

                    master_data.get_datapoint_53_display(),
                    master_data.get_datapoint_54_display(),


                    master_data.is_datapoint_55,
                    master_data.is_datapoint_56,
                    master_data.is_datapoint_57,
                    master_data.is_datapoint_58,
                    master_data.is_datapoint_59,

                    master_data.is_datapoint_60,

                    master_data.is_datapoint_61,

                    master_data.datapoint_62,

                    master_data.is_datapoint_63,
                    master_data.is_datapoint_64,

                    master_data.get_datapoint_65_display(),

                    master_data.is_datapoint_66,

                    master_data.get_datapoint_67_display(),

                    master_data.get_datapoint_68_display(),

                    master_data.is_datapoint_69,
                    master_data.is_datapoint_70,
                    master_data.is_datapoint_71,


                    master_data.get_datapoint_72_display(),
                    master_data.get_datapoint_73_display(),

                    master_data.is_datapoint_74,
                    master_data.is_datapoint_75,


                    master_data.is_datapoint_76,
                    master_data.is_datapoint_77,
                    master_data.is_datapoint_78,


                    master_data.is_datapoint_79,
                    master_data.is_datapoint_80,

                    master_data.is_datapoint_81,
                    master_data.is_datapoint_82,
                    master_data.is_datapoint_83,


                    master_data.get_datapoint_84_display(),

                    master_data.get_datapoint_85_display(),

                    master_data.get_datapoint_86_display(),

                    master_data.is_datapoint_87,

                    master_data.datapoint_88,

                    master_data.is_datapoint_89,

                    master_data.is_datapoint_90,

                    master_data.is_datapoint_91,

                    master_data.get_datapoint_92_display(),

                    master_data.get_datapoint_93_display(),

                    master_data.get_datapoint_94_display(),

                    master_data.is_datapoint_95,

                    master_data.datapoint_96,

                    master_data.is_datapoint_97,

                    master_data.is_datapoint_98,

                    master_data.get_datapoint_99_display(),

                    master_data.get_datapoint_100_display(),

                    master_data.get_datapoint_101_display(),

                    master_data.get_datapoint_102_display(),
                    master_data.datapoint_103,
                    master_data.is_datapoint_104,
                    master_data.is_datapoint_105,
                    master_data.is_datapoint_106,
                    master_data.is_datapoint_107,
                    master_data.is_datapoint_108,
                    master_data.is_datapoint_109,
                    master_data.is_datapoint_110,
                    master_data.is_datapoint_111,
                    master_data.is_datapoint_112,

                    master_data.is_datapoint_113,

                    master_data.is_datapoint_114,

                    master_data.is_datapoint_115,

                    master_data.is_datapoint_116,

                    master_data.is_datapoint_117,

                    master_data.is_datapoint_118,

                    master_data.is_datapoint_119

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
                ws.write(row_num, a.__next__(), master_data.is_datapoint_8,             font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_9_display(),    font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_10_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_11_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_12_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_13_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_14_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_15,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_16,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_16_b_display(), font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_16_b_display(), font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_17_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_18,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_19,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_20,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_21_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_22_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_23,            font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_24,               font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_25,               font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_26,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_27_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_28,               font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_29,               font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_30,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_31_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_32_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_33_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_34_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_35_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_36_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_37_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_38_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_39,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_40_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_41_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_42,            font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_43,               font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_44,               font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_45,               font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_46,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_47,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_48,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_49,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_50,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_51_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_52_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_53_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_54_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_55,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_56,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_57,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_58,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_59,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_60,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_61,            font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_62,               font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_63,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_64,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_65_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_66,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_67_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_68_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_69,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_70,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_71,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_72_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_73_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_74,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_75,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_76,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_77,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_78,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_79,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_80,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_81,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_82,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_83,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_84_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_85_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_86_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_87,            font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_88,               font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_89,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_90,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_91,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_92_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_93_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_94_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_95,            font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_96,               font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_97,            font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_98,            font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_99_display(),   font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_100_display(),  font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_101_display(),  font_style)
                ws.write(row_num, a.__next__(), master_data.get_datapoint_102_display(),  font_style)
                ws.write(row_num, a.__next__(), master_data.datapoint_103,              font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_104,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_105,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_106,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_107,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_108,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_109,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_110,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_111,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_112,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_113,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_114,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_115,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_116,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_117,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_118,           font_style)
                ws.write(row_num, a.__next__(), master_data.is_datapoint_119,           font_style)


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

def master_table_view(request):
    if request.method == "GET":

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

            search_param['pacient__email'] = email

        if nsh_id:
            nsh_id = str(nsh_id)

            search_param['pacient__nsh_id'] = nsh_id

        if first_name:
            first_name = vaidator_data.validate_firstname(str(first_name))

            search_param['pacient__first_name'] = first_name

        if last_name:
            print(last_name)
            last_name = vaidator_data.validate_firstname(str(last_name))
            print(last_name)
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



        master_table = MasterTable.objects.filter(**search_param).order_by('id')[:50]
        return render(request,'masterTable/masterTable.html',{
            'master_table':master_table,'user':request.user,
        })


# def createPacient(request):
#
#     if request.method == "GET":
#
#     elif request.method == "POST":
#         try:
#             nsh_id_old = Pacient.objects.all().order_by('-id')[0]
#             print(nsh_id_old)
#             nsh_id_old = str(nsh_id_old.nsh_id)
#
#             print(str(nsh_id_old))
#             nsh_id_new = gen_aaaannnna(nsh_id_old)
#         except:
#             nsh_id_new = gen_aaaannnna()
#
#         new_pacient = Pacient.objects.create(
#             email="s.hones@gmail.com",
#             phone="380953958123",
#             first_name="Sherlok",
#             last_name="Homes",
#             default_city="London",
#             home_addres="Baker str 13 a",
#             date_of_birth="1987-02-23"
#         )
#
#         new_pacient.nsh_id = nsh_id_new
#         new_pacient.save()
#
#     return "ok"


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
            first_name = vaidator_data.validate_firstname(str(first_name))

            search_param['first_name'] = first_name

        if last_name:
            print(last_name)
            last_name = vaidator_data.validate_firstname(str(last_name))
            print(last_name)
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

        if nsh_id:
            nsh_id = str(nsh_id)

            search_param['nsh_id'] = nsh_id

        if first_name:
            first_name = vaidator_data.validate_firstname(str(first_name))

            search_param['first_name'] = first_name

        if last_name:
            print(last_name)
            last_name = vaidator_data.validate_firstname(str(last_name))
            print(last_name)
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