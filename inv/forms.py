from django import forms

from .models import Categoria,SubCategoria


class CategoriaForm(forms.ModelForm):    
    class Meta:
        model=Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripcion de la Categoría",
               "estado": "Estado"}
        widget={'descripcion' : forms.TextInput}
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class' :'form-control'
                })

class SubCategoriaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset=Categoria.objects.filter(estado=True).order_by('descripcion')
    )
    class Meta:
        model=SubCategoria
        fields = ['categoria','descripcion', 'estado']
        labels = {'descripcion': "Sub Categoría",
               "estado": "Estado"}
        widget={
            'descripcion' : forms.TextInput,
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class' :'form-control'
                })
            self.fields['categoria'].empty_label = "Seleccione Categoría"