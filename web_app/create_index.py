import time
from pymysql import connect, cursors


def create_b_tree_index():
    start_tic = time.perf_counter()

    connection = connect(
        host='localhost', user='user', password='123', database='db_test', cursorclass=cursors.DictCursor
    )

    sql_query = 'CREATE INDEX `birth_date_index` USING BTREE ON `users` (`birth_date`);'
    with connection.cursor() as cursor:
        result = cursor.execute(sql_query)
        print(result)
        connection.commit()

    end_tic = time.perf_counter()
    print(f"B-Tree Index created in {end_tic - start_tic:0.4f} seconds")


def create_hash_index():
    start_tic = time.perf_counter()

    connection = connect(
        host='localhost', user='user', password='123', database='db_test', cursorclass=cursors.DictCursor
    )

    sql_query = 'CREATE INDEX `birth_date_index` USING HASH ON `users` (`birth_date`);'
    with connection.cursor() as cursor:
        result = cursor.execute(sql_query)
        print(result)
        connection.commit()

    end_tic = time.perf_counter()
    print(f"Hash Index created in {end_tic - start_tic:0.4f} seconds")


def drop_index():
    start_tic = time.perf_counter()

    connection = connect(
        host='localhost', user='user', password='123', database='db_test', cursorclass=cursors.DictCursor
    )

    sql_query = 'DROP INDEX `birth_date_index` ON `users`;'
    with connection.cursor() as cursor:
        result = cursor.execute(sql_query)
        print(result)
        connection.commit()

    end_tic = time.perf_counter()
    print(f"Index dropped in {end_tic - start_tic:0.4f} seconds")


# drop_index()
# create_b_tree_index()
# create_hash_index()
