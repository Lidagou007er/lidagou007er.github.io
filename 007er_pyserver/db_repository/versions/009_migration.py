from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
conceptions = Table('conceptions', pre_meta,
    Column('conception_id', VARCHAR(length=25), primary_key=True, nullable=False),
    Column('conception_id2', VARCHAR(length=25)),
    Column('conception_title', VARCHAR(length=25)),
    Column('conception_content', TEXT),
    Column('conception_style', VARCHAR(length=25)),
    Column('conception_gv_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['conceptions'].columns['conception_id2'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['conceptions'].columns['conception_id2'].create()
