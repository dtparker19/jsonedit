from django.shortcuts import render
from .models import JsonDocument
from .forms import DynamicJsonForm, JsonPairFormSet
import json
def json_editor(request):
    template = get_object_or_404(JsonTemplate, user=request.user)
    if request.method == 'POST':
        form = DynamicJsonForm(request.POST, template=template)
        if form.is_valid():
            json_data = {name: form.cleaned_data[name] for name in form.fields}
            # Save or process your json_data here
    else:
        form = DynamicJsonForm(template=template)
    return render(request, 'json_editor.html', {'form': form})
