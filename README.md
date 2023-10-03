# Miceli Processos

Este projeto é uma aplicação web moderna desenvolvida com Django, Django REST Framework e React Vite. Ele consiste em um backend Django que oferece uma API RESTful e um frontend React Vite que consome essa API.

## Pré-requisitos

Antes de começar, você precisa ter o Python, Django, Node.js e npm instalados em seu sistema. Certifique-se de ter um ambiente Python virtual configurado para o backend Django.

## Configuração do Backend

1. **Clone este repositório:**
   ```bash
   git clone <URL_DO_SEU_REPOSITORIO>

2. **Navegue até o repositório do projeto:**
   ```bash
   cd nome-do-seu-projeto

3. **Crie um ambiente virtual para o Django e ative-o:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Para sistemas baseados em Unix/Linux

4. **Aplique as migrações do banco de dados:**
   ```bash
   python manage.py migrate

5.**Crie um superusuário para acessar o painel de administração Django:**
   ```bash
   python manage.py createsuperuser

6.**Inicie o server django:**
   ```bash
   python manage.py runserver

7.**Acesse o painel de administração Django em http://localhost:8000/admin/ e faça login com suas credenciais de superusuário.**
