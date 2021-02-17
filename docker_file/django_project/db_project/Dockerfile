FROM mysql:5.7

ENV MYSQL_ALLOW_EMPTY_PASSWORD true
ENV MYSQL_DATABASE mydb

COPY db_mount /var/lib/mysql 

EXPOSE 3306

CMD ["mysqld"]