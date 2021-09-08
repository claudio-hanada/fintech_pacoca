import math

from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render

class homeView(TemplateView):
    template_name = 'home.html'

class resultView(TemplateView):
    template_name = 'result.html'

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        mensalidade = request.POST.get('mensalidade')
        tempo = int(request.POST.get('tempo'))
        juros = 0
        # taxa esta com valor ao ano
        taxa = 1.90
        #M = C (1 + i)t
        
        if tempo == 1:
            tempo = '6 meses'
            juros = math.pow(1 + taxa, 0.5)
        elif tempo == 2:
            tempo = '12 meses'
            juros = math.pow(1 + taxa, 1)
        elif tempo == 2:
            tempo = '18 meses'
            juros = math.pow(1 + taxa, 1.5)
        else:
            tempo = '24 meses'
            juros = math.pow(1 + taxa, 2)

        expectativa = int(mensalidade) * juros
        
        data = {
            'nome': nome,
            'mensalidade': "{:.2f}".format(float(mensalidade)),
            'tempo': tempo,
            'expectativa': "{:.2f}".format(float(expectativa))
        }
        return render(request, self.template_name, {'data':data})
