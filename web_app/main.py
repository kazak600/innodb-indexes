import logging
import random
import uuid
from aiohttp import web
from datetime import datetime
from pymysql import connect, cursors

routes = web.RouteTableDef()

# innodb_adaptive_hash_index=ON
# innodb_adaptive_hash_index=OFF
# b-tree or hash index
# user concurrency for innodb_flush_log_at_trx_commit=0/1/2


@routes.get('/')
async def index(request):
    return web.json_response({'status': 'OK', 'page': 'index'})


@routes.get('/create_table')
async def create_table(request):
    connection = request.app['db']

    sql_query = """CREATE TABLE `users` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `email` varchar(255) COLLATE utf8_bin NOT NULL,
        `password` varchar(255) COLLATE utf8_bin NOT NULL,
        `birth_date` datetime,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
    AUTO_INCREMENT=1 ;"""

    with connection.cursor() as cursor:
        cursor.execute(sql_query)

    return web.json_response({'status': 'OK', 'action': 'create table'})


@routes.get('/insert')
async def insert(request):
    connection = request.app['db']
    sql_query = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s);"
    with connection.cursor() as cursor:
        password = str(random.randint(1, 99999999))
        user = str(uuid.uuid4())
        birth_date = datetime(1971, 1, 1)
        result = cursor.execute(sql_query, (user, password))

    return web.json_response({'status': 'OK', 'page': 'insert users'})


@routes.get('/get')
async def get_users(request):
    connection = request.app['db']
    sql_query = "select count(*) from `users`;"
    with connection.cursor() as cursor:
        result = cursor.execute(sql_query)
        print(result)

    return web.json_response({'result': result})


def main():
    app = web.Application()
    app.add_routes(routes)
    # for docker host='mysql'
    app['db'] = connect(host='localhost', user='user', password='123', database='db_test', cursorclass=cursors.DictCursor)

    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app)


if __name__ == '__main__':
    main()
