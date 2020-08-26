from django.shortcuts import render,redirect
from .forms import KaryawanForm
from .models import karyawan

# Create your views here.
def home(request):
	return render(request, 'karyawan/home.html' ,{})

def daftar_karyawan(request):
	context = {'daftar_karyawan':karyawan.objects.all()}
	return render(request,"karyawan/daftar_karyawan.html",context)

def form_karyawan(request,id=0):
	if request.method == "GET":
		if id==0:
			form = KaryawanForm()
		else: 
			Karyawan = karyawan.objects.get(pk=id)
			form = KaryawanForm(instance=Karyawan)
		return render(request,"karyawan/form_karyawan.html",{'form':form})
	else:
		if id ==0:
			form = KaryawanForm(request.POST)
		else:
			Karyawan = karyawan.objects.get(pk=id)
			form = KaryawanForm(request.POST,instance = Karyawan)
		if form.is_valid():
			form.save()
		return redirect('/karyawan/daftar/')

def karyawan_delete(request,id):
	Karyawan = karyawan.objects.get(pk=id)
	Karyawan.delete()
	return redirect('/karyawan/daftar/')