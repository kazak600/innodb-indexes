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


def main():
    app = web.Application()
    app.add_routes(routes)
    # for docker host='mysql'
    app['db'] = connect(host='localhost', user='user', password='123', database='db_test', cursorclass=cursors.DictCursor)

    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app)


if __name__ == '__main__':
    main()
