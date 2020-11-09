from django.shortcuts import render

from django.http import HttpResponse

from .models import (
    MasterTable,
    Pacient,
    gen_aaaannnna
)

def master_table_view(request):

    master_table = MasterTable.objects.filter().order_by('id')[:20]
    return render(request,'masterTable/masterTable.html',{
        'master_table':master_table,
    })


def index(request):

    try:
        nsh_id_old = Pacient.objects.all().order_by('-id')[0]
        print(nsh_id_old)
        nsh_id_old = str(nsh_id_old.nsh_id)

        print(str(nsh_id_old))
        nsh_id_new = gen_aaaannnna(nsh_id_old)
    except:
        nsh_id_new = gen_aaaannnna()




    new_pacient  = Pacient.objects.create(
        email="s.hones@gmail.com",
        phone="380953958123",
        first_name="Sherlok",
        last_name="Homes",
        default_city="London",
        home_addres="Baker str 13 a",
        date_of_birth="1987-02-23"
    )






    new_pacient.nsh_id = nsh_id_new
    new_pacient.save()


    return HttpResponse("Hello, world. You're at the polls index.")

