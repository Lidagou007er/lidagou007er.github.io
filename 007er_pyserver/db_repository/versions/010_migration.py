from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
gv__files = Table('gv__files', post_meta,
    Column('gv_id', Integer, primary_key=True, nullable=False),
    Column('gv_title', String(length=25)),
    Column('gv_abstract', TEXT),
    Column('gv_content', TEXT),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['gv__files'].columns['gv_abstract'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['gv__files'].columns['gv_abstract'].drop()
