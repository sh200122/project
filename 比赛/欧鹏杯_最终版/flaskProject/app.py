from flask import *

import bankdata as ba
import function as func

app = Flask(__name__)


# 首页
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# 故事
@app.route('/story', methods=['GET', 'POST'])
def story():
    return render_template('story.html')


# 故事1
@app.route('/story1', methods=['GET', 'POST'])
def storyDetail1():
    return render_template('storyDetail1.html')


# 更多故事
@app.route('/moreStorys', methods=['GET', 'POST'])
def moreStorys():
    return render_template('moreStorys.html')

# 热点1
@app.route('/hot01', methods=['GET', 'POST'])
def hot01():
    return render_template('hot01.html')

# 热点2
@app.route('/hot02', methods=['GET', 'POST'])
def hot02():
    return render_template('hot02.html')

# 热点3
@app.route('/hot03', methods=['GET', 'POST'])
def hot03():
    return render_template('hot03.html')

# 热点4
@app.route('/hot04', methods=['GET', 'POST'])
def hot04():
    return render_template('hot04.html')

# 热点5
@app.route('/hot05', methods=['GET', 'POST'])
def hot05():
    return render_template('hot0.html')

# 热点6
@app.route('/hot06', methods=['GET', 'POST'])
def hot06():
    return render_template('hot06.html')


# 更多英雄
@app.route('/moreHeros', methods=['GET', 'POST'])
def moreHeros():
    return render_template('moreHeros.html')



# 英雄1
@app.route('/hero01', methods=['GET', 'POST'])
def hero01():
    return render_template('hero01.html')


# 英雄2
@app.route('/hero02', methods=['GET', 'POST'])
def hero02():
    return render_template('hero02.html')

# 英雄3
@app.route('/hero03', methods=['GET', 'POST'])
def hero03():
    return render_template('hero03.html')

# 英雄4
@app.route('/hero04', methods=['GET', 'POST'])
def hero04():
    return render_template('hero04.html')

# 英雄5
@app.route('/hero05', methods=['GET', 'POST'])
def hero05():
    return render_template('hero05.html')


# 英雄6
@app.route('/hero06', methods=['GET', 'POST'])
def hero06():
    return render_template('hero06.html')


# 资料
@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

# 资料1
@app.route('/about1', methods=['GET', 'POST'])
def about1():
    return render_template('about1.html')

# 资料2
@app.route('/about2', methods=['GET', 'POST'])
def about2():
    return render_template('about2.html')

# 资料3
@app.route('/about3', methods=['GET', 'POST'])
def about3():
    return render_template('about3.html')

# 资料4
@app.route('/about4', methods=['GET', 'POST'])
def about4():
    return render_template('about4.html')

# 个人中心
@app.route('/user', methods=['GET', 'POST'])
def user():
    id=request.args.get('id')
    return render_template('user.html',id=id)


# 注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    idlst = ba.updata.idlst()
    if request.method == 'POST':
        ID = request.form['ID']  # 根据id属性值获取对应标签中的值
        password = request.form['password']
        password1 = request.form['tpassword']
        print(ID, password)
        if ID in idlst:
            if password.strip() == password1.strip():
                return render_template('register.html', message='账号已存在！请重新输入')
            else:
                return render_template('register.html', message='两次输入的密码不一致!')
        else:
            # 存入数据库
            func.register(ID, password)
            return redirect('/')  # 重新进入登录的路由
    return render_template('register.html', message='')


# 信息完善
@app.route('/message_ws', methods=['GET', 'POST'])
def message_ws():
    id1 = str(request.args.get('id'))

    if request.method == 'POST':
        nc = request.form['nc']  # 根据id属性值获取对应标签中的值
        xb = request.form['xb']  # 根据id属性值获取对应标签中的值
        nl = request.form['nl']  # 根据id属性值获取对应标签中的值
        jx = request.form['jx']  # 根据id属性值获取对应标签中的值
        bk = request.form['bk']  # 根据id属性值获取对应标签中的值
        yx = request.form['yx']  # 根据id属性值获取对应标签中的值
        jj = request.form['jj']
        print(nc, xb, nl, jx, bk,jj)
        # 存入数据库
        func.message_ws(id1, nc, xb, nl, jx, bk, yx,jj)
    return render_template('message_ws.html', id=id1)



# 收藏夹
@app.route('/shoucangjia', methods=['GET', 'POST'])
def shoucangjia():
    return render_template('shoucangjia.html')


#个人简介
@app.route('/introdu', methods=['GET', 'POST'])
def introdu():
        # 获取传过来的id值
        id = request.args.get('id')
        print(id,type(id))
        if id is not None:
        # nc = ba.updata(id).search_nc()
        # xb = ba.updata(id).search_xb()
        # nl = ba.updata(id).search_nl()
        # jx = ba.updata(id).search_jx()
        # bk = ba.updata(id).search_bk()
        # yx = ba.updata(id).search_yx()
        # jj = ba.updata(id).search_jj()
        # , xb = xb, nl = nl, jx = jx, bk = bk, yx = yx, jj = jj
            return render_template('introdu.html', nc=func.search_nc(id,0),xb=func.search_nc(2),nl=func.search_nc(id,3),jx=func.search_nc(id,4),bk=func.search_nc(id,5),yx=func.search_nc(id,6),jj=func.search_nc(id,7))
        return render_template('introdu.html',message='这人很懒，没留下任何东西，只留下了光……')

# 捐款
@app.route('/jk_index', methods=['GET', 'POST'])
def jk():
    return render_template('jk_index.html')


# 二维码
@app.route('/jk_afford', methods=['GET', 'POST'])
def jk_afford():
    return render_template('jk_afford.html')


# 尾部1
@app.route('/ed1', methods=['GET', 'POST'])
def end1():
    return render_template('ed1.html')

# 尾部2
@app.route('/ed2', methods=['GET', 'POST'])
def end2():
    return render_template('ed2.html')

# 尾部3
@app.route('/ed3', methods=['GET', 'POST'])
def end3():
    return render_template('ed3.html')

# 尾部4
@app.route('/ed4', methods=['GET', 'POST'])
def end4():
    return render_template('ed4.html')


# 尾部5
@app.route('/ed5', methods=['GET', 'POST'])
def end5():
    return render_template('ed5.html')


# 关于1
@app.route('/about_2_1', methods=['GET', 'POST'])
def about_2_1():
    return render_template('about_2_1.html')


# 关于2
@app.route('/about_2_2', methods=['GET', 'POST'])
def about_2_2():
    return render_template('about_2_2.html')



# 关于3
@app.route('/about_2_3', methods=['GET', 'POST'])
def about_2_3():
    return render_template('about_2_3.html')


# 关于4
@app.route('/about_2_4', methods=['GET', 'POST'])
def about_2_4():
    return render_template('about_2_4.html')



# 关于5
@app.route('/about_2_5', methods=['GET', 'POST'])
def about_2_5():
    return render_template('about_2_5.html')



# 关于3_1
@app.route('/about_3_1', methods=['GET', 'POST'])
def about_3_1():
    return render_template('about_3_1.html')


# 关于3_2
@app.route('/about_3_2', methods=['GET', 'POST'])
def about_3_2():
    return render_template('about_3_2.html')

# 关于3_3
@app.route('/about_3_3', methods=['GET', 'POST'])
def about_3_3():
    return render_template('about_3_3.html')


# 关于4_1
@app.route('/about_4_1', methods=['GET', 'POST'])
def about_4_1():
    return render_template('about_4_1.html')


# 关于4_2
@app.route('/about_4_2', methods=['GET', 'POST'])
def about_4_2():
    return render_template('about_4_2.html')

# 关于4_3
@app.route('/about_4_3', methods=['GET', 'POST'])
def about_4_3():
    return render_template('about_4_2.html')


# 政策
@app.route('/privacy-policy', methods=['GET', 'POST'])
def privacy_policy():
    return render_template('privacy-policy.html')



# 使用条款
@app.route('/terms-of-use', methods=['GET', 'POST'])
def terms_of_usey():
    return render_template('terms-of-use.html')



# 登录页面
@app.route('/', methods=['GET', 'POST'])
def login():
    idlst = ba.updata.idlst()
    if request.method == 'POST':
        ID = request.form['ID']  # 根据id属性值获取对应标签中的值
        password = request.form['password']

        if ID in idlst:
            a = ba.updata(id=ID)
            user = a.search_user_datas()
            # print(user)
            if password == user[2]:
                user = a.search_user_datas()
                return render_template('index.html', user=user,id=a.id)
            elif password.strip() == "":
                return render_template('login.html', message='密码不能为空！')
            else:
                return render_template('login.html', message='账号或密码错误！')
        elif ID.strip() == "" and password.strip() != "":
            return render_template('login.html', message='用户不能为空！')
        elif ID.strip() == "" or password.strip() == "":
            return render_template('login.html', message='用户或密码不能为空！')
        elif ID.strip() != "" and password.strip() == "":
            return render_template('login.html', message='密码不能为空！')
        else:
            return render_template('login.html', message='账号或密码错误！')
    return render_template('login.html', message='')




# 菜单
@app.route('/dashboard')
def dashboard():
    user = ba.updata.search_user_datas()
    return render_template('dashboard.html', user=user)





# 退出登录
@app.route('/logout')
def logout():
    return redirect('/')


# 修改用户数据
@app.route('/updata_user_main')
def update_users():
    user = ba.updata.search_user_datas()
    return render_template('update_user.html', user=user)


@app.route('/updata_user', methods=['POST'])
def update_user():
    user = ba.updata.search_user_datas()
    ID = user[0]
    if request.method == "POST":
        password = request.form['password']
        name = request.form['name']
        tlpno = request.form['tlpno']
        adrs = request.form['adrs']
        ba.updata.update_datas(ID=ID, name=name, password=password, tlpno=tlpno, adrs=adrs)
        user = ba.updata.search_user_datas()
        return render_template('find_users_datas.html', user=user, message='已成功修改!')


# 销户
@app.route('/account_closure/<ID>')
def account_closure(ID):
    ba.updata.account_closure(ID=ID)
    return redirect('/')


# 存款
@app.route('/deposit_main')
def a():
    user = ba.updata.search_user_datas()
    return render_template('chun.html', user=user)


@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == "POST":
        mane = 0
        mane = request.form['chun']
        user = ba.updata.search_user_datas()
        if int(mane) <= 0:
            return render_template('chun.html', message='存款金额不能为负数!', user=user)
        else:
            ba.updata.deposit(mane)
            user = ba.updata.search_user_datas()
            return render_template('dashboard.html', user=user)


# 取款
@app.route('/withdrawal_main')
def b():
    user = ba.updata.search_user_datas()
    return render_template('qu.html', user=user)


@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == "POST":
        mane = request.form['qu']
        user = ba.updata.search_user_datas()
        if int(mane) <= 0:
            return render_template('qu.html', message='取款金额不能为负数!', user=user)
        else:
            if int(mane) >= int(user[7]):
                return render_template("dashboard.html", user=user)
            else:
                ba.updata.withdraw(mane)
                user1 = ba.updata.search_user_datas()
                return render_template("dashboard.html", user=user1)


# 查询交易记录

@app.route('/recording')
def recording():
    a = func.search_record()
    return render_template('find_recording.html', a=a)


# 转账
@app.route('/transfer_main')
def transfers():
    user = ba.updata.search_user_datas()
    return render_template('transfer.html', user=user)


@app.route('/transfer', methods=['POST'])
def transfer():
    if request.method == "POST":
        mane = request.form['mane']
        zrID = request.form['zrID']
        user = ba.updata.search_user_datas()
        if int(mane) <= 0:
            return render_template('transfer.html', message='转账金额不能为负数!', user=user)
        else:
            if int(mane) >= int(user[7]):
                return render_template("dashboard.html", user=user)
            else:
                ba.updata.transfer(mane=mane, zrID=zrID)
                user1 = ba.updata.search_user_datas()
                return render_template("dashboard.html", user=user1)


# 查看存款类型
@app.route('/find_type')
def find_type():
    type = list(ba.updata.search_type().values())[0]
    return render_template('type.html', type=type)


# 挂失
@app.route('/loss')
def loss():
    ba.updata.loss()
    user1 = ba.updata.search_user_datas()
    return redirect('/dashboard')


# 解挂
@app.route('/un_loss')
def un_loss():
    ba.updata.un_loss()
    return redirect('/dashboard')


# 挂失警告
@app.route('/alert')
def alert():
    user = ba.updata.search_user_datas()
    return render_template('dashboard.html', user=user, alert='您的账户已挂失，请解除后重试！！')


if __name__ == '__main__':
    app.run(debug=True)
