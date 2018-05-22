from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from ordem.models import ordens
from contas.models import conta
from produto.models import produto

# Create your views here.
def home(request):
    if request.user.is_authenticated():
        try:
            ordem_aberta = ordens.objects.filter(estado=1).count()
        except:
            ordem_aberta = 0
        prod = 0
        contas = 0
        hoje = timezone.now()
        for e in conta.objects.filter(estado=1).all():
            if e.data <= timezone.now():
                contas = contas + 1
            else:
                contas = contas

        for p in produto.objects.all():
            if p.quantidade <= p.qnt_min:
                prod = prod + 1
            else:
                prod = prod
        n_ordem = ordem_aberta
        n_contas =  contas
        n_produto = prod
        return render(request, 'home/index.html', {'title':'Home', 'n_ordem':n_ordem, 'n_contas':n_contas, 'hoje':hoje, 'n_produto':n_produto})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def outros(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('senha') != None:
            password = request.POST.get('senha')
            user = authenticate(username='jean', password=password)
            if user is not None:
                if user.is_active:
                    return render(request, 'home/outros1.html', {'title':'Outros'})
            msg = "Senha Invalida"
            return render(request, 'home/index.html', {'title':'Outros', 'msg':msg})
        return render(request, 'home/outros.html', {'title':'Outros'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})