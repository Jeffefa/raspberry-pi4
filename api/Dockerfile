FROM python:3.13.5-slim

# Evita que o Python escreva arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
# Evita buffer nos logs
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código fonte
COPY ./src /app/src

# Expõe a porta do uvicorn
EXPOSE 8000

# Executa a API com hot-reload (para desenvolvimento)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
