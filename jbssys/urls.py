from django.urls import path, include
from jbssys import views

urlpatterns = [

    path('login/',views.login_view,name='login_view'),
    path('sign_up/',views.register_view,name='register_view'),
    path('master/',views.master_table_view, name="master_table_view"),
    path('pacients/', views.pacientsView, name="pacientsView"),
    path('pacients/download/',views.pacientDownloadFile,name='pacientDownloadFile'),
    path('master/download/', views.master_tableDownloadFile, name='master_tableDownloadFile'),



]