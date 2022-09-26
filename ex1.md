# Create MYSQL container

    docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -e MYSQL_DATABASE=test -e MYSQL_USER=test -e MYSQL_PASSWORD=test -d mysql

# Create MYSQL client

    docker run -it --rm logiqx/mysql-client mysql --host=HOSTNAME --database=DATABASE --user=USERNAME --password
