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

## Django X Aplicações

Cada projeto engloba o todo e pode ter várias aplicações aplicações plugáveis. Essas aplicações plugáveis podem ser utilizadas em mais de um projeto.

## Padrão MTV do Django

- **User -> Sistema**: Browser -> URLs -> Views -> Models (ORM) -> Banco de Dados
- **Sistema -> User**: Banco de dados -> Models -> Views -> Templates -> Browser





