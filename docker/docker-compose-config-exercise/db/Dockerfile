# Derived from official mysql image (our base image)
FROM mysql:5.7

# Add a database

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup
ENV MYSQL_DATABASE=flask-db
ENV MYSQL_ROOT_PASSWORD=root
COPY ./CreateTable.sql /docker-entrypoint-initdb.d/
