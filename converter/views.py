import json
from django.http import JsonResponse
from django.views.generic import CreateView
from converter.forms import ConverterForm
from converter.converter import Convert


class ConverterView(CreateView):

    form_class = ConverterForm
    template_name = 'index.html'

    def get_form_kwargs(self):
        kwargs = super(ConverterView, self).get_form_kwargs()
        if self.request.method in ('POST', 'PUT'):
            kwargs['data'] = json.loads(self.request.body)
        return kwargs

    def form_valid(self, form):

        obj = form.save(commit=False)
        converter = Convert(obj.input_number)
        obj.output_number = converter.convert()
        obj.save()
        return JsonResponse({"result": obj.output_number})

    def form_invalid(self, form):
        return JsonResponse(dict(form.errors.items()), status=400)

