from django import forms
from .models import Departameto,Computadora,Propiedad,LectorCD_DVD,MemoriaRam,Discos

#Formulario de Departamento Empresa
class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departameto
        fields = ['nombre','cantidad_pc']
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'cantidad_pc':forms.TextInput(attrs={'class':'form-control'})
        }

class ComputadoraForm(forms.ModelForm):
    class Meta:
        model = Computadora
        fields = ['componente_pc','num_inventario','marca','estado','numero_pc','departamento']
        widgets = {
            'componente_pc':forms.TextInput(attrs={'class':'form-control'}),
            'num_inventario':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.TextInput(attrs={'class':'form-control'}),
            'numero_pc':forms.TextInput(attrs={'class':'form-control'}),
            'departamento':forms.Select(attrs={'class':'form-control'})
        }

class MemoriaRamForm(forms.ModelForm):
    class Meta:
        model = MemoriaRam
        fields=['clasificacion','capacidad','marca','velocidad']
        widgets = {
            'clasificacion':forms.TextInput(attrs={'class':'form-control'}),
            'capacidad':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'velocidad':forms.TextInput(attrs={'class':'form-control'})
        }

class DiscoForm(forms.ModelForm):
    class Meta:
        model = Discos
        fields=['clasificacion','capacidad','marca','serie']
        widgets = {
            'clasificacion':forms.TextInput(attrs={'class':'form-control'}),
            'capacidad':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.TextInput(attrs={'class':'form-control'}),
            'serie':forms.TextInput(attrs={'class':'form-control'})
        }
class LectorForm(forms.ModelForm):
    class Meta:
        model=LectorCD_DVD
        fields=['clasificacion','marca']
        widgets = {
            'clasificacion':forms.TextInput(attrs={'class':'form-control'}),
            'marca':forms.TextInput(attrs={'class':'form-control'})
        }

class PropiedadForm(forms.ModelForm):
    class Meta:
        model=Propiedad
        fields=['procesador','lista_memorias_ram','lista_discos_duros','gpu','computadora']
        widgets = {
            'procesador':forms.TextInput(attrs={'class':'form-control'}),
            'memoria_ram':forms.TextInput(attrs={'class':'form-control'}),
            'disco':forms.TextInput(attrs={'class':'form-control'}),
            'gpu':forms.TextInput(attrs={'class':'form-control'}),
            'computadora':forms.Select(attrs={'class':'form-control'})
        }
