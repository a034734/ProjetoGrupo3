# Projeto do Grupo 3: This or That

## Pré-requisitos
- Django
- Python
- Virtual Env

## Como instalar o Python:
Para fazer o download e a instalação do Python é apenas aceder ao seguinte link e seguir as instruções:
https://www.python.org/downloads/

## Como instalar o pip e o Virtual Env:

1º Upgrade do pip:

    C:\Users\Daniel>py -m pip install --upgrade pip
  
2º Download e instalação do Virtual Environment:

    C:\Users\Daniel>pip install virtualenv
  
## Como entrar no Virtual Env:

1º Criação da Virtual Env: 
  
    C:\Users\Daniel>py -m venv teste
  
2º Entrar na Virtual Env:
    
    C:\Users\Daniel>teste\Scripts\activate

3º Instalar o Django:

    (teste) C:\Users\Daniel>pip install django
    Collecting django
    Downloading Django-3.0.6-py3-none-any.whl (7.5 MB)
     |████████████████████████████████| 7.5 MB 3.3 MB/s

## Como instalar o site e inserir na localização certa:

1º Download da pasta "mysite", que está localizada na home deste projeto do GitHub, para instalar, clique no botão "Clone or download" e selecione a opção "Download ZIP"

2º Colocar a pasta no mesmo sítio da Virtual Env, ou seja, C:\Users\(nome do utilizador)

3º Entrar no diretório "mysite":
    
    (teste) C:\Users\Daniel>cd mysite

4º Instalar o Crispy Forms:

    (teste) C:\Users\Daniel\mysite>pip install django-crispy-forms
    Collecting django-crispy-forms
    Downloading django_crispy_forms-1.9.1-py2.py3-none-any.whl (108 kB)
     |████████████████████████████████| 108 kB 2.2 MB/s

5º Fazer as migrações necessárias:

    (teste) C:\Users\Daniel\mysite>py manage.py makemigrations
    (teste) C:\Users\Daniel\mysite>py manage.py migrate

6º Iniciar o servidor:
  
    (teste) C:\Users\Daniel\mysite>py manage.py runserver
    
 Depois de fazer este comando copiar o link desta linha:
   
    Starting development server at http://127.0.0.1:8000/

Para aceder ao site, use o link com o adicional /home
Exemplo: http://127.0.0.1:8000/home/

## Para mais quaisquer dúvidas sobre a instalação aceda a este vídeo:
        https://www.youtube.com/watch?v=FTgqmgREsCQ

## Objetivo:
O site This or That tem como principal objetivo a construção de um jogo em que o utilizador escolha a imagem que prefere entre duas oferecidas. O site tem tanto jogos criados pelos criadores, tanto jogos criados pelos utilizadores (como fossem jogos da comunidade). A plataforma é simples e facíl de utilizar, possibilitanto o utilizador jogar sem dificuldades.

## Ferramentas de Trabalho:
### Editor de código fonte:
Front end - Visual Studio Code

Back end - Atom
### Sistema para guardar e gerir o projeto:
GitHub

### Editor de fotos e design:
Photoshop

## Desenvolvedores do projeto

Alexandre Nunes - A035528

Daniel Moreira - A034734

Rodrigo Mota - A034729

