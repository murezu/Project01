from django import forms
from .models import karyawan

class KaryawanForm(forms.ModelForm):
	
	class Meta:
		model = karyawan
		fields = ('fullname','alamat','no_hp','jabatan')
		labels = {
			'fullname':'Nama Lengkap',
			'alamat':'Alamat',
			'no_hp':'Nomor Hp',
			'jabatan':'Jabatan'
		}

	def __init__(self, *args, **kwargs):
		super(KaryawanForm,self).__init__(*args, **kwargs)
		self.fields['jabatan'].empty_label = "Select"
		self.fields['jabatan'].required = False