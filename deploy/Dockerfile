# Dockerfile para Minha Vitrine
FROM python:3.11-slim

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Criar diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar projeto
COPY . .

# Criar diretórios necessários
RUN mkdir -p media static

# Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Expor porta
EXPOSE 8000

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

