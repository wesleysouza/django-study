# Django Framework Básico

## Criando um projeto e aplicação

Criando projeto:

```shell
django-admin startproject nome-do-projeto
```

Criando aplicação:

```shell
django-admin startapp nome-da-aplicacao
```

## Criando um arquivo com a lista de dependências

```
pip freeze > requiriments.txt
```

## Aplicação

É um pacote Python.

### Estrutura de uma aplicação

- **migrations**: Forma profissional de manter o histórico de banco de dados.
- **__init__.py**: Define a aplicação em um pacote.
- **admin.py**: Local onde registra-se os modelos para serem administrados.
- **apps.py**: Define o nome da aplicação.
- **models.py**: Onde vão ser criados os modelo de dados (classes), o que vamos persistir no BD.
- **tests.py**: Criar testes para a aplicação.
- **views.py**: Local onde serão definidas as funções que vão ser chamadas nas rotas para abrir os templates para visualização.

Todas as aplicações devem ser registradas no arquivo **settings.py** do projeto na lista **INSTALLED_APPS**.

Os templates também precisam ser configurados, no arquivo **settings.py** na lista **TEMPLATES** adicione o nome diretório **templates** (esse diretório que será criado dentro da aplicação) no campo **DIRS**.

### Registrando uma aplicação

O registro da aplicação no projeto deve ser realizado no arquivo **settings.py** do projeto no campo INSTALLED_APPS. Deve-se observar o nome da classe criada no arquivo apps.py da aplicação.

Exemplo do registro da aplicação Core:

```python
INSTALLED_APPS = [
    
    ...
    
    'core.apps.CoreConfig'
]
``` 

## Django X Aplicações

Cada projeto engloba o todo e pode ter várias aplicações aplicações plugáveis. Essas aplicações plugáveis podem ser utilizadas em mais de um projeto.

## Padrão MTV do Django

- **User -> Sistema**: Browser -> URLs -> Views -> Models (ORM) -> Banco de Dados
- **Sistema -> User**: Banco de dados -> Models -> Views -> Templates -> Browser

## Executando comandos de gerenciamento

Execute os comandos no mesmo diretório do arquivo **manage.py**.

###Executando projeto

Para executar o projeto digite o comando abaixo:

```
python manage.py runserver
``` 

## Views

Uma View é uma função que recebe um parâmetro. Esse parâmetro é uma requisição. O restorno é a rederização do request com um template (uma página html).

## Criando Rotas 

A criação de rotas é no arquivo **urls.py**. Esse arquivo só vem por padrão no projeto. Essas rotas são adicionadas por meio da função **path**.

O ideal é definir as rotas da aplicação criando um arquivo **urls.py** na pasta da aplicação, ou seja, cada aplicação ter o seu arquivo **urls.py** para a definição de suas rotas. Desse modo, no **urls.py** do projeto, será necessário apenas a utilização da função include dentro do path para adicionar todas as rotas de uma determinada aplicação. Em suma, cada aplicação vai ter o seu arquivo de rotas (**urls.py**).

## Templates

Crie o diretório 'templates' (o nome desse diretório foi difinido no arquivo **settings.py** do seu projeto) na sua aplicação. Crie os templates HTML defindos nas Views dentro da pasta.

### Passando informações para os Templates 

As informações podem ser passadas através da View. Ex.:

```python
def index(request):
    context = {
        'curso': 'Programação Web' #Chave:Valor (Dicionário Python)
    }
    return render(request, 'index.html', context)
```

Para exibir o valor no template passe a chave como no exemplo abaixo:

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Django 1 - Index</title>
    </head>
    <body>
        <h1>Index</h1>

        <h2>{{ curso }}</h2>
    </body>
</html>
```

## Area administrativa

A área administrativa é encontrada pelo path /admin.

Criando superusuario:

```
python manage.py createsuperuser
```

Toda aplicação tem um arquivo **admin.py** onde podemos registrar nossos modelos. Exemplo do registro dos modelos Product e Client

```python
from django.contrib import admin

from .models import Product, Client

# Register your models here.
admin.site.register(Product)
admin.site.register(Cliente)
```

Crie função str() no Model para aprensentar o objeto de forma customizada.

```python
class Product(models.Model):
    name = models.CharField('name', max_length=100)
    price = models.DecimalField('price', decimal_places=2, max_digits=8)
    stock = models.IntegerField('stock')

    def __str__(self):
        return self.name
```

Alterando a apresentação do Model Product pelo arquivo **admin.py**:

```python
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(Product, ProductAdmin)
```

### Mudando o path /admin

É possível mudar o nome o path /admin da página admin no arquivo de urls do projeto.

Geralmente, essa modificação é realizada por questões de segurança.

## Django Shell








