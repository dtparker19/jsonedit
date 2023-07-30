from django import forms
import json

class DynamicJsonForm(forms.Form):
    def __init__(self, *args, **kwargs):
        template = kwargs.pop('template', None)
        super(DynamicJsonForm, self).__init__(*args, **kwargs)

        if template:
            for field in template.jsonfield_set.all():
                kwargs = {
                    'required': True,
                    'initial': self.data.get(field.name) if self.data else None,
                }
                if field.data_type == 'str':
                    kwargs['min_length'] = field.min_length
                    kwargs['max_length'] = field.max_length
                    self.fields[field.name] = forms.CharField(**kwargs)
                elif field.data_type == 'int':
                    kwargs['min_value'] = field.min_value
                    kwargs['max_value'] = field.max_value
                    self.fields[field.name] = forms.IntegerField(**kwargs)
                elif field.data_type == 'bool':
                    self.fields[field.name] = forms.BooleanField(**kwargs)
                elif field.data_type == 'float':
                    kwargs['min_value'] = field.min_value
                    kwargs['max_value'] = field.max_value
                    self.fields[field.name] = forms.FloatField(**kwargs)

                if field.choices:
                    self.fields[field.name].choices = json.loads(field.choices)

class JsonPairForm(forms.Form):
    key = forms.CharField()
    value = forms.CharField()

JsonPairFormSet = forms.formset_factory(JsonPairForm, extra=0)
