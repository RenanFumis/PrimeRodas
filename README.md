# Prime Rodas - Car Registration FullStack Project

Welcome to the Car Registration FullStack project! This is a complete application developed in Python using the Django framework. Below you'll find a detailed description of the main features and technologies used.

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, CSS Grid
- **Banco de Dados:** PostgreSQL
- **APIs:** Gemini (for generating car descriptions)
- **Deploy:** AWS

## Features

- **Car Registration:** Register new cars with detailed information and a photo.
- **Automatic Description Generation:** Uses the Gemini API to create automated and detailed descriptions for the registered cars.
- **User Registration:** Users can sign up on the platform and access features to edit and register cars.
- **Error Handling:** Robust implementation to handle search errors and unregistered images, ensuring a smooth user experience.
- **Responsiveness:** 100% responsive design with CSS Grid, adaptable to different screen sizes and devices.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   
2. Navigate to the project directory:
   ```bash
   cd your-repository
   
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt

5. Configure the PostgreSQL database:
   - Update the database settings in **settings.py** with your PostgreSQL credentials.

6. Run database migrations:
   ```bash
   python manage.py migrate

7. Create a superuser to access the Django admin:
   ```bash
   python manage.py createsuperuser

8. Start the development server:
   ```bash
   python manage.py runserver

9. Access the application at: **http://127.0.0.1:8000**

-----------------------------------------------------------------------

# Projeto FullStack de Cadastro de Carros - Prime Rodas

Bem-vindo ao projeto FullStack Prime Rodas! Esta é uma aplicação completa desenvolvida em Python utilizando o framework Django. Abaixo você encontrará uma descrição detalhada das principais funcionalidades e tecnologias utilizadas.

## Tecnologias Utilizadas

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, CSS Grid
- **Banco de Dados:** PostgreSQL
- **APIs:** Gemini (para geração de descrições de carros)
- **Deploy:** AWS

## Funcionalidades

- **Cadastro de Carros:** Registre novos carros com informações detalhadas e uma foto.
- **Geração Automática de Descrição:** Utiliza a API do Gemini para criar descrições automatizadas e detalhadas dos carros cadastrados.
- **Inscrição de Usuários:** Usuários podem se inscrever na plataforma e acessar funcionalidades para editar e registrar carros.
- **Tratamento de Erros:** Implementação robusta para lidar com erros de busca e imagens não registradas, garantindo uma experiência de usuário fluida e sem interrupções.
- **Responsividade:** Design 100% responsivo com CSS Grid, adaptável a diferentes tamanhos de tela e dispositivos.

## Instruções de Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git

2. Navegue até o diretório do projeto:
   ```bash
   cd your-repository
   
3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt

5. Configure o banco de dados PostgreSQL:
   - Atualize as configurações do banco de dados em **settings.py** com suas credenciais do PostgreSQL.

6. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate

7. Crie um superusuário para acessar o admin do Django:
   ```bash
   python manage.py createsuperuser

8. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver

9. Acesse a aplicação em: **http://127.0.0.1:8000**
