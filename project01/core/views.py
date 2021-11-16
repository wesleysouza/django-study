from django.shortcuts import render

from .models import Product

# Create your views here.
def index(request):
    print(dir(request)) # Observando os atributos do objeto request
    print(f'Metodo: {request.method}') # Vendo o método do request
    print(f'Headers: {request.headers}') # Vendo o cabeçalho do request (retorna um dicionário python)
    print(f"User-Agent: {request.headers['User-Agent']}") # Vendo dados do usuário (navegador, SO e etc)
    print(dir(request.user)) # Observando os atributos do objeto user de request
    print(f"User: {request.user}") # Vendo o usuário
    # É necessário que aqui o usuário esteja logado
    #print(f"User LastName: {request.user.last_name}") # Vendo o sobrenome do usuário

    if str(request.user) == 'AnonymousUser':
        test = 'Usuário Não Logado!'
    else:
        test = 'Usuário Logado!'

    #Apresentando produtos do BD na view

    produtos = Product.objects.all()

    context = {
        'curso': 'Programação Web', #Chave:Valor (Dicionário Python)
        'string': 'Mensagem',
        'logado': test,
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')
