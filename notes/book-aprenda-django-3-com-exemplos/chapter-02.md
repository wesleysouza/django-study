#Capítulo 2

##Enviando e-mails com Django

Para enviar e-mails é necessário configurar no arquivo **settings.py** um servidor SMTP. Para simplificar, melhor imprimir os e-mails na saída do terminal adicionando o comando abaixo no arquivo de configuração do projeto:

```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
