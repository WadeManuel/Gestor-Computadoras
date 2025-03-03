from django import forms
from .models import Departameto,Computadora,Invetario

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
        

class InentarioForm(forms.ModelForm):
    class Meta:
        model = Invetario
        fields = ['departamento','pc']
        exclude = ['fecha']