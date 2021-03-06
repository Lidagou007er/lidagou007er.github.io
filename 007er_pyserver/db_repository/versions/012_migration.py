from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
basic__data = Table('basic__data', pre_meta,
    Column('id', VARCHAR(length=25), primary_key=True, nullable=False),
    Column('title', VARCHAR(length=25)),
    Column('abstract', TEXT),
    Column('l1_id', VARCHAR(length=25)),
)

l1__data = Table('l1__data', post_meta,
    Column('id', String(length=25), primary_key=True, nullable=False),
    Column('title', String(length=25)),
    Column('abstract', TEXT),
)

l2__data = Table('l2__data', post_meta,
    Column('id', String(length=25), primary_key=True, nullable=False),
    Column('title', String(length=25)),
    Column('abstract', TEXT),
    Column('l1_id', String(length=25)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['basic__data'].drop()
    post_meta.tables['l1__data'].create()
    post_meta.tables['l2__data'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['basic__data'].create()
    post_meta.tables['l1__data'].drop()
    post_meta.tables['l2__data'].drop()
