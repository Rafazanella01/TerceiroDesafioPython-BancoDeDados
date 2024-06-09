#imagem base do PostgreSQL
FROM postgres:latest

#variáveis de ambiente
ENV POSTGRES_USER root
ENV POSTGRES_PASSWORD root
ENV POSTGRES_DB locadora

#porta padrão do PostgreSQL
EXPOSE 5432