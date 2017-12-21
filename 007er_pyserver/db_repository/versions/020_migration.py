from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
the__writer = Table('the__writer', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('id007', String(length=25)),
    Column('name', String(length=25)),
    Column('city', String(length=25)),
    Column('phone_num', String(length=25)),
    Column('official_account', String(length=25)),
    Column('tags', String(length=25)),
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
    post_meta.tables['the__writer'].columns['city'].create()
    post_meta.tables['the__writer'].columns['hobbies'].create()
    post_meta.tables['the__writer'].columns['me_after_7_years'].create()
    post_meta.tables['the__writer'].columns['my_expect'].create()
    post_meta.tables['the__writer'].columns['official_account'].create()
    post_meta.tables['the__writer'].columns['others'].create()
    post_meta.tables['the__writer'].columns['phone_num'].create()
    post_meta.tables['the__writer'].columns['reason'].create()
    post_meta.tables['the__writer'].columns['sth_i_provide'].create()
    post_meta.tables['the__writer'].columns['sth_i_want'].create()
    post_meta.tables['the__writer'].columns['tags'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['the__writer'].columns['city'].drop()
    post_meta.tables['the__writer'].columns['hobbies'].drop()
    post_meta.tables['the__writer'].columns['me_after_7_years'].drop()
    post_meta.tables['the__writer'].columns['my_expect'].drop()
    post_meta.tables['the__writer'].columns['official_account'].drop()
    post_meta.tables['the__writer'].columns['others'].drop()
    post_meta.tables['the__writer'].columns['phone_num'].drop()
    post_meta.tables['the__writer'].columns['reason'].drop()
    post_meta.tables['the__writer'].columns['sth_i_provide'].drop()
    post_meta.tables['the__writer'].columns['sth_i_want'].drop()
    post_meta.tables['the__writer'].columns['tags'].drop()
