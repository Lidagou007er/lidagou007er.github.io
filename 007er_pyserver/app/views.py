# -*- coding:utf-8 -*-


from flask import (
    request,make_response)
from app.models import The_Writer
from app import app, db
import json
from functools import wraps



#===cross_domain====
'''这个是允许跨域的代码'''

def allow_cross_domain(fun):

    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst

    return wrapper_fun
#===    end     ===

#===    end     ===
#======index.html=======
'''这里是index中用到的API接口'''

@app.route('/get_my_info',methods=['POST'])
@allow_cross_domain
def get_my_info():
    the_id=msg_translate_from_front(request)['id']
    the_info=The_Writer.query.filter_by(id007=the_id).all()
    return msg_traslate_to_front(the_info)

@app.route('/save_my_info',methods=['POST'])
@allow_cross_domain
def save_my_info():
    a_writer=The_Writer()
    a_writer.id007=msg_translate_from_front(request)['id']

    a_writer.name=msg_translate_from_front(request)['name']
    a_writer.city=msg_translate_from_front(request)['city']
    a_writer.phone_num=msg_translate_from_front(request)['phonenum']
    a_writer.official_account=msg_translate_from_front(request)['offcialaccount']
    a_writer.tags=msg_translate_from_front(request)['tags']
    a_writer.others=msg_translate_from_front(request)['others']
    a_writer.hobbies=msg_translate_from_front(request)['hobbies']
    a_writer.sth_i_provide=msg_translate_from_front(request)['sthiprovide']
    a_writer.sth_i_want=msg_translate_from_front(request)['sthiwant']
    a_writer.reason=msg_translate_from_front(request)['reason']
    a_writer.my_expect=msg_translate_from_front(request)['myexpect']
    a_writer.me_after_7_years=msg_translate_from_front(request)['meafter7years']

    db.session.add(a_writer)
    db.session.commit()
    return a_writer.id007

#===    end     ===

#=== black code ===

'''Python格式=>前端数据'''
def msg_traslate_to_front(msg_all):
    try:
        msg_after_trans={msg_all[0].class_name:[]}

        for every_msg in msg_all:
            a_msg={}

            for every_vary in every_msg.class_varies:
                a_msg[every_vary]=every_msg.get_vary(every_vary)

            msg_after_trans[msg_all[0].class_name].append(a_msg)

        json_data=json.dumps(msg_after_trans)
        print("translate_to_front is {0}".format(json_data))
        #data format:{posts:[{a:b,c:d},{a:e,c:f}...]}
        return json_data
    except:
        return None

'''前端数据=>Python格式'''
def msg_translate_from_front(request):
    msg_data_old=request.form.to_dict()
    for i in msg_data_old:
        msg_data_new= json.loads(i)
    print("translate_from_front is {0}".format(msg_data_new))
    return msg_data_new

#===    end     ===

