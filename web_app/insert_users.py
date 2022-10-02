import time
import random
import uuid
from datetime import datetime
from pymysql import connect, cursors


def insert_users():
    start_tic = time.perf_counter()

    connection = connect(
        host='localhost', user='user', password='123', database='db_test', cursorclass=cursors.DictCursor
    )

    users_count = 100_000

    arguments = []
    for _ in range(users_count):
        user = str(uuid.uuid4())
        password = str(random.randint(1, 99999999))

        year = random.randint(1920, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        birth_date = datetime(year, month, day)
        arguments.extend([user, password, birth_date])

    values = ','.join(['(%s, %s, %s)' for _ in range(users_count)])
    sql_query = f"""INSERT INTO `users` (`email`, `password`, `birth_date`) VALUES {values};"""

    with connection.cursor() as cursor:
        result = cursor.execute(sql_query, arguments)
        print(result)
        connection.commit()

    end_tic = time.perf_counter()
    print(f"Insert in {end_tic - start_tic:0.4f} seconds")


for i in range(400):
    insert_users()
