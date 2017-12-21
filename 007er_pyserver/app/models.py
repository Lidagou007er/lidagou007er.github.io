# -*- coding:utf-8  -*-

from app import db

class The_Writer(db.Model):
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.Integer,primary_key=True)
    id007=db.Column(db.String(25))
    name=db.Column(db.String(25))

    city=db.Column(db.String(25))
    phone_num=db.Column(db.String(25))
    official_account=db.Column(db.String(25))
    tags=db.Column(db.String(25))
    others= db.Column(db.TEXT)
    hobbies = db.Column(db.TEXT)
    sth_i_provide = db.Column(db.TEXT)
    sth_i_want = db.Column(db.TEXT)
    reason = db.Column(db.TEXT)
    my_expect= db.Column(db.TEXT)
    me_after_7_years = db.Column(db.TEXT)

    class_name = "the_writer"
    class_varies = ['id', 'id007', 'name', 'city','phone_num','official_account','tags','others'\
                    ,'hobbies','sth_i_provide','sth_i_want','reason','my_expect','me_after_7_years']
    def get_vary(self, vary_name):
        return eval("self." + vary_name)




