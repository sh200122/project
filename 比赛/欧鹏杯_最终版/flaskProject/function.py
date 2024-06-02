import bankdata as ba
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
from flask import request, session
import calendar

# 注册
def register(id,password):
    # lst = ['name', 'id', 'tlpno', 'adrs', 'ID', 'password']
    # data_lst = []
    # for item in lst:
    #     data_lst.append(request.form.get(f'{item}'))
    # ba.bankdatas.__init__(data_lst[0], data_lst[1], data_lst[2], data_lst[3],
    #             data_lst[4], data_lst[5]).add_datas()
    ba.updata(id).add_datas(password)


# 信息完善
def message_ws(id,nc, xb,nl,jx,bk,yx,jj):
    ba.updata(id).add_message(nc, xb,nl,jx,bk,yx,jj)



# 查询个人信息
def search_user_data():
    # data_lst = ba.updata('', '', '', '', '', '', '').search_user_datas()
    data_lst=ba.updata.search_user_datas()
    return data_lst


# 查询昵称
def search_nc(id,i):
    # data_lst = ba.updata('', '', '', '', '', '', '').search_user_datas()
    data_lst=ba.updata(id).search_nc(i)
    return data_lst

#
# # 查询性别
# def search_xb(id):
#     # data_lst = ba.updata('', '', '', '', '', '', '').search_user_datas()
#     data_lst=ba.updata(id).search_xb()
#     return data_lst
#
# # 查询年龄
# def search_nl(id):
#     # data_lst = ba.updata('', '', '', '', '', '', '').search_user_datas()
#     data_lst=ba.updata(id).search_nl()
#     return data_lst
#
# # 查询家乡
# def search_jx(id):
#     # data_lst = ba.updata('', '', '', '', '', '', '').search_user_datas()
#     data_lst=ba.updata(id).search_jx()
#     return data_lst
#
# # 查询家乡
# def search_jx(id):
#     # data_lst = ba.updata('', '', '', '', '', '', '').search_user_datas()
#     data_lst=ba.updata(id).search_jx()
#     return data_lst
#
# # 查询家乡
# def search_jx(id):
#     # data_lst = ba.updata('', '', '', '', '', '', '').search_user_datas()
#     data_lst=ba.updata(id).search_jx()
#     return data_lst
#
#
# # 查询家乡
# def search_jx(id):
#     # data_lst = ba.updata('', '', '', '', '', '', '').search_user_datas()
#     data_lst=ba.updata(id).search_jx()
#     return data_lst


# 查询家乡
def search_jx(id):
    # data_lst = ba.updata('', '', '', '', '', '', '').search_user_datas()
    data_lst=ba.updata(id).search_jx()
    return data_lst


# 查询家乡
def search_jx(id):
    # data_lst = ba.updata('', '', '', '', '', '', '').search_user_datas()
    data_lst=ba.updata(id).search_jx()
    return data_lst






# 修改
def update_user_data(ID,name,password,tlpno,adrs):
    # course_lst = ['password','name','tlpno','adrs','pid']
    # update_lst = []
    # for item in course_lst:
    #     update_lst.append(request.form.get(f'{item}'))
    # print(update_lst)
    # ba.updata(ID=ID, password=update_lst[0], name=update_lst[1], tlpno=update_lst[2], adrs=update_lst[3],pid=update_lst[4]).update_datas()
    ba.updata.update_datas(ID=ID,name=name,password=password,tlpno=tlpno,adrs=adrs)

def search_record():
    datalist=ba.updata.search_recording()
    return datalist

def search_type():
    type=ba.updata.search_type()
    return type