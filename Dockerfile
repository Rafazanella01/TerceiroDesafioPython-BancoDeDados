#imagem base do PostgreSQL
FROM postgres:latest

# Defina variáveis de ambiente para o Postgres
ENV POSTGRES_USER root
ENV POSTGRES_PASSWORD root
ENV POSTGRES_DB bd

#porta padrão do PostgreSQL
EXPOSE 5432