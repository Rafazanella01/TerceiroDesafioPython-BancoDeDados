# Use a imagem oficial do MySQL
FROM mysql:5.7

# Defina variáveis de ambiente
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=root

# Exponha a porta 3306
EXPOSE 3306