import time
from pymysql import connect, cursors


def get_users():
    start_tic = time.perf_counter()
    connection = connect(
        host='localhost', user='user', password='123', database='db_test', cursorclass=cursors.DictCursor
    )

    sql_query = "select count(*) from `users` where birth_date > '1931-1-1' and birth_date < '1991-1-1';"
    print(f'SQL: {sql_query}')

    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        result = cursor.fetchall()

    for user in result:
        print(user)

    end_tic = time.perf_counter()
    print(f"Select in {end_tic - start_tic:0.4f} seconds")


get_users()
