from pymysql import connect, cursors


def create_table():
    connection = connect(
        host='localhost', user='user', password='123', database='db_test', cursorclass=cursors.DictCursor
    )

    sql_query = """CREATE TABLE `users` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `email` varchar(255) COLLATE utf8_bin NOT NULL,
        `password` varchar(255) COLLATE utf8_bin NOT NULL,
        `birth_date` date,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
    AUTO_INCREMENT=1 ;"""

    with connection.cursor() as cursor:
        result = cursor.execute(sql_query)
        print(result)
        connection.commit()


create_table()
