# -*- coding: utf-8 -*-

import asyncio
from aiohttp import web
from database import create_db, close_db
import api


def make_app(loop):
    app = web.Application(loop=loop)

    app.on_startup.append(create_db)
    app.on_cleanup.append(close_db)

    app.router.add_get('/todos/{id:\d+}', api.get_one_todo, name='get_one_todo')
    app.router.add_patch('/todos/{id:\d+}', api.update_todo, name='update_todo')
    app.router.add_delete('/todos/{id:\d+}', api.remove_todo, name='remove_todo')
    app.router.add_get('/todos', api.get_all_todo, name='get_all_todo')
    app.router.add_post('/todos', api.create_todo, name='create_todo')

    return app


def run_server():
    loop = asyncio.get_event_loop()

    app = make_app(loop)
    handler = app.make_handler()

    loop.run_until_complete(app.startup())
    server = loop.create_server(handler, 'localhost', 8080)
    srv = loop.run_until_complete(server)
    try:
        loop.run_forever()
    finally:
        srv.close()
        loop.run_until_complete(srv.wait_closed())
        loop.run_until_complete(app.shutdown())
        loop.run_until_complete(handler.shutdown(60.0))
        loop.run_until_complete(app.cleanup())
    loop.close()


if __name__ == '__main__':
    run_server()
