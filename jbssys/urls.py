from django.urls import path, include
from jbssys import views

urlpatterns = [

    path('login/',views.login_view,name='login_view'),
    path('sign_up/',views.register_view,name='register_view'),

    path('master/',views.master_table_view, name="master_table_view"),
    path('pacients/', views.pacientsView, name="pacientsView"),

    path('datadictionary/del/<str:req_id>/', views.data_dictionatyDelete, name='data_dictionatyDelete'),
    path('datadictionary/', views.data_dictionaty, name="data_dictionaty"),
    path('datadictionary/edit/<str:req_id>/', views.data_dictionatyEdit, name='data_dictionatyEdit'),
    path('datadictionaty/load/',views.data_dictionaty_load,name='data_dictionaty_load'),


    path('pacient/del/<str:req_id>/', views.pacientDelete, name='pacientDelete'),
    path('pacients/download/',views.pacientDownloadFile,name='pacientDownloadFile'),
    path('master/download/', views.master_tableDownloadFile, name='master_tableDownloadFile'),
    path('master/download/templates/',views.master_tableDownloadFileTemps,name='master_tableDownloadFileTemps'),

    path('pacients/load/',views.pacientDownLoadFile,name='pacientDownLoadFile'),
    path('master/load/', views.master_tableLoadFile, name='master_tableLoadFile'),




]

