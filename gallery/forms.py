from django import forms
from .models import Gallery, GalleryCategory


# Gallery form

class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ('user_name', 'email', 'author_name',
                  'gallery_category', 'image', 'note',)

    def __init__(self, *args, **kwargs):
        """
            Set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        gallerycategories = GalleryCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in gallerycategories]

        self.fields['gallery_category'].choices = friendly_names

        self.fields['user_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-grey'
