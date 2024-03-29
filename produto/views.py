from django.shortcuts import render
from django.contrib.auth import authenticate
from produto.models import produto

# Create your views here.
def produto1(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('name'):
            name = request.POST.get('name')
            valor_vend = request.POST.get('valor_vend')
            valor_comp = request.POST.get('valor_comp')
            qnt = request.POST.get('qnt')
            qnt_min = request.POST.get('qnt_min')
            novo_produto = produto(nome=name, valor_venda=valor_vend, valor_compra=valor_comp, qnt_min=qnt_min, quantidade=qnt)
            novo_produto.save()
            return render(request, 'produto.html', {'title':'Produto'})
        return render(request, 'produto.html', {'title':'Produto'})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def busca1(request):
    if request.user.is_authenticated():
        pro1 = produto.objects.all()
        if request.method == 'GET' and request.GET.get('p_id') != None:
            prod_id = request.GET.get('p_id')
            prods = produto.objects.filter(id=prod_id).get()
            return render(request, 'busca_produto.html', {'title':'Busca Produto', 'prods':prods})
        elif request.method == 'POST':
            produto_id = request.POST.get('id')
            produto_obj = produto.objects.filter(id=produto_id).get()

            return render(request, 'edit_produto.html', {'title':'Editar Produto', 'produto_obj':produto_obj})
        return render(request, 'busca_produto.html', {'title':'Busca Produto', 'pro1':pro1})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})

def editar1(request):
    if request.user.is_authenticated():
        if request.method == 'POST' and request.POST.get('id') != None:
            produto_id = request.POST.get('id')
            produto_obj = produto.objects.filter(id=produto_id).get()
            produto_nome = request.POST.get('name')
            produto_valor = request.POST.get('valor_vend')
            produto_qnt = request.POST.get('qnt')
            prod_valor_comp = request.POST.get('valor_comp')
            produto_qnt_min = request.POST.get('qnt_min')
            produto_obj.nome = produto_nome
            produto_obj.valor_venda = produto_valor
            produto_obj.quantidade = produto_qnt
            produto_obj.valor_compra = prod_valor_comp
            produto_obj.qnt_min = produto_qnt_min
            produto_obj.save()
            msg = "Produto editado com sucesso."
            return render(request, 'home/index.html', {'title':'Home', 'msg':msg})
    else:
        return render(request, 'home/erro.html', {'title':'Erro'})