from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'curso': 'Programação Web', #Chave:Valor (Dicionário Python)
        'string': 'Mensagem'
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
