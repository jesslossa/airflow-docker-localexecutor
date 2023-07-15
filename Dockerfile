# Usa a base image do Python para o Airflow
FROM python:3.8-slim-buster

# Define as variáveis de ambiente
ENV AIRFLOW_HOME=/opt/airflow
ENV AIRFLOW__CORE__EXECUTOR=LocalExecutor
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres:5432/airflow

# Atualiza o sistema operacional e instala as dependências necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libffi-dev \
    libssl-dev \
    libpq-dev \
    && apt-get clean

# Instala o Airflow
RUN pip install --no-cache-dir "apache-airflow==2.6.3" \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.6.3/constraints-3.8.txt"

# Copia o arquivo requirements.txt para o container
COPY requirements.txt .

# Instala as bibliotecas especificadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Inicializa o banco de dados do Airflow
RUN airflow db init

# Cria um usuário admin
RUN airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com \
    --password admin

# Expõe a porta 8080 para o webserver do Airflow
EXPOSE 8080

# Define o diretório de trabalho como AIRFLOW_HOME
WORKDIR ${AIRFLOW_HOME}

# Inicia o webserver do Airflow
CMD ["airflow", "webserver", "--port", "8080"]
