# -*- coding: utf-8 -*-

from aiohttp.web import json_response, Response
from sqlalchemy import sql
from model.todo import tbl_todo

__all__ = [
    'get_all_todo', 'get_one_todo',
    'create_todo', 'remove_todo', 'update_todo'
]


async def get_all_todo(request):
    """
    get all todo
    """
    async with request.app['db'].acquire() as conn:
        all_todo = []
        async for row in conn.execute(
                tbl_todo.select().order_by(tbl_todo.c.id)):
            all_todo.append(dict(row.items()))
        return json_response(all_todo)


async def get_one_todo(request):
    """
    get todo by id
    """
    _id = int(request.match_info['id'])
    async with request.app['db'].acquire() as conn:
        result = await conn.execute(
            tbl_todo.select().where(tbl_todo.c.id == _id))
        row = await result.fetchone()

    if not row:
        return json_response({'error': 'Todo not found'}, status=404)

    return json_response(dict(row.items()))


async def create_todo(request):
    """
    create a new todo
    """
    data = await request.json()

    if 'content' not in data:
        return json_response({'error': '"content" is a required field'})

    content = data['content']

    if not content or not isinstance(content, str):
        return json_response(
            {'error': '"name" must be a string with at least one character'})

    todo = {'content': content, 'finished': data.get('finished', 'no')}

    async with request.app['db'].acquire() as conn:
        async with conn.begin():
            await conn.execute(
                tbl_todo.insert().values(todo))
            result = await conn.execute(
                sql.select([sql.func.max(tbl_todo.c.id).label('id')])
            )
            new_id = await result.fetchone()

    return Response(
        status=303,
        headers={
            'Location': str(request.app.router['get_one_todo'].url_for(id=new_id.id))
        }
    )


async def remove_todo(request):
    """
    remove todo by id
    """
    _id = int(request.match_info['id'])

    async with request.app['db'].acquire() as conn:
        result = await conn.execute(
            tbl_todo.delete().where(tbl_todo.c.id == _id))

    if not result.rowcount:
        return json_response({'error': 'Todo not found'}, status=404)

    return Response(status=204)


async def update_todo(request):
    """
    update todo status by id
    """
    _id = int(request.match_info['id'])
    data = await request.json()

    if 'finished' not in data:
        return json_response(
            {'error': '"finished" is a required key'}, status=400)

    async with request.app['db'].acquire() as conn:
        result = await conn.execute(
            tbl_todo.update().where(tbl_todo.c.id == _id).values({
                'finished': data['finished']
            })
        )

    if result.rowcount == 0:
        return json_response({'error': 'Todo not found'}, status=404)

    return Response(status=204)
