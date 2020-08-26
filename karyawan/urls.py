from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name='home'),
    path('tambah', views.form_karyawan,name='karyawan_insert'), #get dan post request. buat insert data
    path('<int:id>/', views.form_karyawan,name='karyawan_update'), #get dan post request untuk update data
    path('hapus/<int:id>/',views.karyawan_delete,name='karyawan_delete'),
    path('daftar/',views.daftar_karyawan,name='daftar_karyawan') #get dan request untuk menerima data dari database (DAFTAR E)
]
