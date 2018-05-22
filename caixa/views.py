from django.shortcuts import render
from caixa.models import caixa_geral
from ordem.models import ordens
from decimal import *
from datetime import datetime, timedelta

# Create your views here.
def caixa1(request):
    if request.user.is_authenticated():
        try:
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total
        except:
            caixa = caixa_geral(tipo=1, total=0, desc="abertura")
            caixa.save()
            total = caixa.total
        entrada = caixa_geral.objects.filter(tipo=1).count()
        saida = caixa_geral.objects.filter(tipo=2).count()
        return render(request, 'caixa.html', {'title':'Caixa', 'total':total, 'entrada':entrada, 'saida':saida})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def retirada(request):
    if request.user.is_authenticated():
        try:
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total
        except:
            caixa = caixa_geral(tipo=1, total=0, desc="abertura")
            caixa.save()
            total = caixa.total
        if request.method == 'POST' and request.POST.get('retirada') != None:
            valor_ret = request.POST.get('retirada')
            desc = request.POST.get('motivo')
            total = caixa.total - Decimal(valor_ret)
            nova_op = caixa_geral(total=total, tipo=2, desc=desc)
            nova_op.save()
            msg = "Retirada concluida com sucesso."
            return render(request, 'home/index.html', {'title':'Home', 'msg':msg})
        return render(request, 'retirada.html', {'title':'Retirada', 'total':total})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def fechar(request):
    if request.user.is_authenticated():
        try:
            caixa = caixa_geral.objects.latest('id')
            total = caixa.total
        except:
            caixa = caixa_geral(tipo=1, total=0, desc="abertura")
            caixa.save()
            total = caixa.total
        if request.method == 'POST' and request.POST.get('retirada') != None:
            valor_ret = request.POST.get('retirada')
            desc = 'Fechamento'
            total = caixa.total - Decimal(valor_ret)
            nova_op = caixa_geral(total=total, tipo=2, desc=desc)
            nova_op.save()
            msg = "Fechamento concluido com sucesso."
            return render(request, 'home/index.html', {'title':'Home', 'msg':msg})
        return render(request, 'fechar.html', {'title':'Retirada', 'total':total})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def inf_geral(request):
    if request.user.is_authenticated():
        caixa = caixa_geral.objects.latest('id')
        caixa_1 = caixa_geral.objects.get(id=1)
        dia_1 = caixa_1.data.strftime('%d/%m/%Y')
        total_dim = 0
        total_cd = 0
        total_cc = 0
        
        for a in ordens.objects.filter(estado=2, metodo=1).all():
            total_dim = total_dim + a.total
        for b in ordens.objects.filter(estado=2, metodo=2).all():
            total_cd = total_cd + b.total
        for c in ordens.objects.filter(estado=2, metodo=3).all():
            total_cc = total_cc + c.total
        
        return render(request, 'info_geral.html', {'title':'Informacao Geral', 'dia_1':dia_1, 'total_dim':total_dim, 'total_cd':total_cd, 'total_cc':total_cc, 'caixa':caixa, 'dia_1':dia_1})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def inf_mens(request):
    if request.user.is_authenticated():
        caixa = caixa_geral.objects.latest('id')
        dia_1 = datetime.today()
        dia_2 = dia_1 - timedelta(days=30)
        total_mens = 0
        rec_mens = 0
        total_dim = 0
        total_cd = 0
        total_cc = 0
        for a in ordens.objects.filter(estado=1, data_fechamento__lte=dia_1, data_fechamento__gt=dia_2).all():
            total_mens = total_mens + a.total
        for b in ordens.objects.filter(estado=2, data_fechamento__lte=dia_1, data_fechamento__gt=dia_2).all():
            rec_mens = rec_mens + b.total
        for c in ordens.objects.filter(estado=2, metodo=1, data_fechamento__lte=dia_1, data_fechamento__gt=dia_2).all():
            total_dim = total_dim + c.total
        for d in ordens.objects.filter(estado=2, metodo=2, data_fechamento__lte=dia_1, data_fechamento__gt=dia_2).all():
            total_cd = total_cd + d.total
        for e in ordens.objects.filter(estado=2, metodo=3, data_fechamento__lte=dia_1, data_fechamento__gt=dia_2).all():
            total_cc = total_cc + e.total
        total_rec = total_mens - rec_mens
        return render(request, 'info_men.html', {'title':'Informacao Mensal','dia_1':dia_1, 'dia_2':dia_2, 'total_dim':total_dim, 'total_cd':total_cd, 'total_cc':total_cc, 'total_mens':total_mens, 'dia_1':dia_1, 'rec_mens':rec_mens, 'total_rec':total_rec})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})