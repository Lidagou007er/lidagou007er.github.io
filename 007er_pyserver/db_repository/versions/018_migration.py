from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
the__writer = Table('the__writer', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('id007', VARCHAR(length=25), primary_key=True, nullable=False),
    Column('name', VARCHAR(length=25)),
    Column('city', VARCHAR(length=25)),
    Column('phone_num', VARCHAR(length=25)),
    Column('official_account', VARCHAR(length=25)),
    Column('tags', VARCHAR(length=25)),
    Column('others', TEXT),
    Column('hobbies', TEXT),
    Column('sth_i_provide', TEXT),
    Column('sth_i_want', TEXT),
    Column('reason', TEXT),
    Column('my_expect', TEXT),
    Column('me_after_7_years', TEXT),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['the__writer'].columns['city'].drop()
    pre_meta.tables['the__writer'].columns['hobbies'].drop()
    pre_meta.tables['the__writer'].columns['me_after_7_years'].drop()
    pre_meta.tables['the__writer'].columns['my_expect'].drop()
    pre_meta.tables['the__writer'].columns['official_account'].drop()
    pre_meta.tables['the__writer'].columns['others'].drop()
    pre_meta.tables['the__writer'].columns['phone_num'].drop()
    pre_meta.tables['the__writer'].columns['reason'].drop()
    pre_meta.tables['the__writer'].columns['sth_i_provide'].drop()
    pre_meta.tables['the__writer'].columns['sth_i_want'].drop()
    pre_meta.tables['the__writer'].columns['tags'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['the__writer'].columns['city'].create()
    pre_meta.tables['the__writer'].columns['hobbies'].create()
    pre_meta.tables['the__writer'].columns['me_after_7_years'].create()
    pre_meta.tables['the__writer'].columns['my_expect'].create()
    pre_meta.tables['the__writer'].columns['official_account'].create()
    pre_meta.tables['the__writer'].columns['others'].create()
    pre_meta.tables['the__writer'].columns['phone_num'].create()
    pre_meta.tables['the__writer'].columns['reason'].create()
    pre_meta.tables['the__writer'].columns['sth_i_provide'].create()
    pre_meta.tables['the__writer'].columns['sth_i_want'].create()
    pre_meta.tables['the__writer'].columns['tags'].create()
