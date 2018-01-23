# -*- coding: utf-8 -*-

from aiomysql.sa import create_engine
from config import config


async def create_db(app):
    '''
    create db engine
    '''
    app['db'] = await create_engine(
        host=config['host'],
        port=config['port'],
        user=config['user'],
        password=config['password'],
        db=config['db'],
        minsize=2,
        autocommit=True,
        charset='utf8'
    )


async def close_db(app):
    '''
    close db engine
    '''
    app['db'].close()
    await app['db'].wait_closed()
    app['db'] = None
