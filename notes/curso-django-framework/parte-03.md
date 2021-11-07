#Django Framework Básico

## Criando um projeto e aplicação

Criando projeto:

ˋˋˋshell
django-admin startproject nome-do-projeto
ˋˋˋ 

Criando aplicação:

ˋˋˋshell
django-admin startapp nome-da-aplicacao
ˋˋˋ 

## Criando um arquivo com a lista de dependências

ˋˋˋ
pip freeze > requiriments.txt
ˋˋˋ 

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

ˋˋˋpython
INSTALLED_APPS = [
    
    ...
    
    'core.apps.CoreConfig'
]
ˋˋˋ 

## Django X Aplicações

Cada projeto engloba o todo e pode ter várias aplicações aplicações plugáveis. Essas aplicações plugáveis podem ser utilizadas em mais de um projeto.

## Padrão MTV do Django

- **User -> Sistema**: Browser -> URLs -> Views -> Models (ORM) -> Banco de Dados
- **Sistema -> User**: Banco de dados -> Models -> Views -> Templates -> Browser

## Executando comandos de gerenciamento

Execute os comandos no mesmo diretório do arquivo **manage.py**.

###Executando projeto

Para executar o projeto digite o comando abaixo:

ˋˋˋ
python manage.py runserver
ˋˋˋ 

## Views

Uma View é uma função que recebe um parâmetro. Esse parâmetro é uma requisição. O restorno é a rederização do request com um template (uma página html).

## Criando Rotas 

A criação de rotas é no arquivo **urls.py**. Esse arquivo só vem por padrão no projeto. Essas rotas são adicionadas por meio da função **path**.

O ideal é definir as rotas da aplicação criando um arquivo **urls.py** na pasta da aplicação, ou seja, cada aplicação ter o seu arquivo **urls.py** para a definição de suas rotas. Desse modo, no **urls.py** do projeto, será necessário apenas a utilização da função include dentro do path para adicionar todas as rotas de uma determinada aplicação. Em suma, cada aplicação vai ter o seu arquivo de rotas (**urls.py**).

## Templates

Crie o diretório 'templates' (o nome desse diretório foi difinido no arquivo **settings.py** do seu projeto) na sua aplicação. Crie os templates HTML defindos nas Views dentro da pasta.

### Passando informações para os Templates 

As informações podem ser passadas através da View. Ex.:

ˋˋˋpython
def index(request):
    context = {
        'curso': 'Programação Web' #Chave:Valor (Dicionário Python)
    }
    return render(request, 'index.html', context)
ˋˋˋ

Para exibir o valor no template passe a chave como no exemplo abaixo:

ˋˋˋhtml
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
ˋˋˋ











