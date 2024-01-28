# Use a imagem oficial do Python como base
FROM python:3.8-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos necessários para instalação do projeto
COPY requirements.txt .

# Ativa amb. virtual e instala as dependências
RUN python -m venv venv
RUN /bin/bash -c "source ./venv/bin/activate"
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos para o diretório de trabalho
COPY . .

# Expõe a porta em que o Flask irá rodar
EXPOSE 5000

# Define a variável de ambiente para o Flask
ENV FLASK_APP=__init__.py

# Comando para executar o aplicativo Flask quando o container for iniciado
CMD ["flask", "--app", "src", "run" ,"--host=0.0.0.0"]
