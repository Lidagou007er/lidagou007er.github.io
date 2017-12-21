from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
conceptions = Table('conceptions', pre_meta,
    Column('conception_id', VARCHAR(length=25), primary_key=True, nullable=False),
    Column('conception_title', VARCHAR(length=25)),
    Column('conception_content', TEXT),
    Column('conception_style', VARCHAR(length=25)),
    Column('conception_gv_id', INTEGER),
)

gv__files = Table('gv__files', pre_meta,
    Column('gv_id', INTEGER, primary_key=True, nullable=False),
    Column('gv_title', VARCHAR(length=25)),
    Column('gv_content', TEXT),
    Column('gv_abstract', TEXT),
)

relationships = Table('relationships', post_meta,
    Column('id', String(length=25), primary_key=True, nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['conceptions'].drop()
    pre_meta.tables['gv__files'].drop()
    post_meta.tables['relationships'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['conceptions'].create()
    pre_meta.tables['gv__files'].create()
    post_meta.tables['relationships'].drop()
