from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
conceptions = Table('conceptions', post_meta,
    Column('conception_id', Integer, primary_key=True, nullable=False),
    Column('conception_id2', String(length=25)),
    Column('conception_title', String(length=25)),
    Column('conception_content', TEXT),
    Column('conception_style', String(length=25)),
    Column('conception_gv_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['conceptions'].columns['conception_id2'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['conceptions'].columns['conception_id2'].drop()
