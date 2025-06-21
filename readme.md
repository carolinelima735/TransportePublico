 Como rodar o projeto
1. Crie um ambiente virtual
Windows:

python -m venv venv
venv\Scripts\activate

Linux/macOS:

python3 -m venv venv
source venv/bin/activate

2. Instale as dependências

pip install -r requirements.txt

Se não tiver um arquivo requirements.txt, rode:

pip install django djangorestframework pandas scikit-learn

3. Inicie o servidor Django

python manage.py migrate
python manage.py runserver

O servidor será iniciado em:

cpp


http://127.0.0.1:8000/

📂 Endpoint da API

1. Via Postman ou Insomnia:

Método: POST

URL: http://localhost:8000/api/analisar/

Body → form-data

Key: file

Type: File

Value: selecione o transporte.csv



Descrição:
Este endpoint recebe um arquivo CSV com as colunas linha e quantidade_passageiros e devolve um JSON classificando cada linha em Baixa, Média ou Alta demanda, usando clusterização automática com KMeans.




🛠 Como gerar o requirements.txt:

Se ainda não criou, basta rodar este comando no terminal com o ambiente virtual ativado:
pip freeze > requirements.txt

Isso vai criar um arquivo com todas as bibliotecas instaladas, pra que qualquer pessoa possa recriar seu ambiente com:
pip install -r requirements.txt
