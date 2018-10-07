import re
from django.core.exceptions import ValidationError

from django.forms import ModelForm
from converter.models import Conversion


class ConverterForm(ModelForm):

    class Meta:
        model = Conversion
        fields = ['input_number']

    def validate_number(self):

        try:
            num_str = self.cleaned_data['input_number']
        except KeyError:
            raise ValidationError('Data should be specified', code=400)

        if num_str.isdigit():
            if not 0 <= int(num_str) <= 3999:
                raise ValidationError('Number should be between 0 and 3999', code=400)
        else:
            number_string = ''.join(num_str.split())
            for char in number_string:
                if char not in "IVXLCDM":
                    raise ValidationError('Enter a valid rome number', code=400)
                else:
                    res = re.fullmatch(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', number_string)
                    if not res:
                        raise ValidationError('Enter a valid rome number', code=400)
        return

    def clean(self):
        self.validate_number()
        return super(ConverterForm, self).clean()

