# -*- coding: utf-8 -*-

import sqlalchemy as sa

metadata = sa.MetaData()

tbl_todo = sa.Table(
    'todo', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('content', sa.String(255), nullable=False),
    sa.Column('finished', sa.Enum('yes', 'no'), default='no', nullable=False)
)
