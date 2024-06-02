import pymysql

conn = pymysql.connect(host="localhost", user="root", password="123456", port=3306, db="aids_web_users_data",charset="utf8",
            cursorclass=pymysql.cursors.DictCursor)

cursor=conn.cursor()



id=''
qu=0
chun=0

class updata:
    def __init__(self,id):
        self.id = id

    def idlst():
        conn.ping(reconnect=True)
        sql_0 = "SELECT id FROM users;"
        cursor.execute(sql_0)
        idlst = cursor.fetchall()
        lst=[]
        for i in idlst:
            lst.append(i['id'])
        return lst

    
    #注册
    def add_datas(self,password):
        # ping()使用该方法 ping(reconnect=True)

        conn.ping(reconnect=True)
        # 编写sql语句
        sql_0 = "INSERT INTO users(id,password) VALUES(%s,%s); "#防止类型与需要的数不一致，用%s确定数据格式为字符型，使用下面一句将数据一一对应传进来
        sql = sql_0 % (repr(self.id),repr(password))

        sql_0 = "INSERT INTO basic_message(id) VALUES(%s); "#防止类型与需要的数不一致，用%s确定数据格式为字符型，使用下面一句将数据一一对应传进来
        sql1 = sql_0 % repr(self.id)
        cursor.execute(sql)
        cursor.execute(sql1)
        # 提交到数据库执行
        conn.commit()
        # 关闭数据库
        conn.close()

    #完善信息
    def add_message(self,nc, xb,nl,jx,bk,yx,jj):
        # ping()使用该方法 ping(reconnect=True)
        conn.ping(reconnect=True)
        print(self.id)
        # 编写sql语句
        # sql_0 = "update basic_message set 昵称=%s,性别=%s,年龄=%s,家乡=%s,博客=%s,邮箱=%s,简介=%s where id="+self.id+";"#防止类型与需要的数不一致，用%s确定数据格式为字符型，使用下面一句将数据一一对应传进来
        sql_0 = "update basic_message set 昵称=%s,性别=%s,年龄=%s,家乡=%s,博客=%s,邮箱=%s,简介=%s;"#防止类型与需要的数不一致，用%s确定数据格式为字符型，使用下面一句将数据一一对应传进来
        sql = sql_0 % (repr(nc),repr(xb),repr(nl),repr(jx),repr(bk),repr(yx),repr(jj))
        # sql_0 = "insert into basic_message (性别,年龄,家乡,博客,邮箱) values (%s,%s,%s,%s,%s,%s)"#防止类型与需要的数不一致，用%s确定数据格式为字符型，使用下面一句将数据一一对应传进来
        # sql = sql_0 % (repr(1),repr(1),repr(1),repr(1),repr(1),repr(1))
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
        # 关闭数据库
        conn.close()


    # 保存用户id到个人简介的表
    def add_datas_m(self, password):
        # ping()使用该方法 ping(reconnect=True)

        conn.ping(reconnect=True)
        # 编写sql语句
        sql_0 = "INSERT INTO basic_message(id) VALUES(%s); "  # 防止类型与需要的数不一致，用%s确定数据格式为字符型，使用下面一句将数据一一对应传进来
        sql = sql_0 % repr(self.id)
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
        # 关闭数据库
        conn.close()


    #查询个人信息
    def search_user_datas(self):
        try:
            ID=self.id
            conn.ping(reconnect=True)
            sql="SELECT * FROM users WHERE id="+ID+";"
            cursor.execute(sql)
            conn.commit()

            result = cursor.fetchall()
            result1 = list(result[0].values())
            # result1[2]=str(result1[2]).split('(')[0]
            return result1
        finally:
            conn.close()


        # 查询昵称
    def search_nc(self,i):
            try:
                ID = self.id
                conn.ping(reconnect=True)
                sql = "SELECT * FROM basic_message WHERE id=" + ID + ";"
                cursor.execute(sql)
                conn.commit()

                result = cursor.fetchall()
                result1 = list(result[i].values())  # 取昵称的值
                # result1[2]=str(result1[2]).split('(')[0]
                return result1
            finally:
                conn.close()

    #     # 查询性别
    # def search_xb(self):
    #         try:
    #             ID = self.id
    #             conn.ping(reconnect=True)
    #             sql = "SELECT * FROM basic_message WHERE id=" + ID + ";"
    #             cursor.execute(sql)
    #             conn.commit()
    #
    #             result = cursor.fetchall()
    #             result1 = list(result[2].values())
    #             # result1[2]=str(result1[2]).split('(')[0]
    #             return result1
    #         finally:
    #             conn.close()
    #
    #     # 查询年龄
    # def search_nl(self):
    #         try:
    #             ID = self.id
    #             conn.ping(reconnect=True)
    #             sql = "SELECT * FROM basic_message WHERE id=" + ID + ";"
    #             cursor.execute(sql)
    #             conn.commit()
    #
    #             result = cursor.fetchall()
    #             result1 = list(result[3].values())
    #             # result1[2]=str(result1[2]).split('(')[0]
    #             return result1
    #         finally:
    #             conn.close()
    #
    #     # 查询家乡
    # def search_jx(self):
    #         try:
    #             ID = self.id
    #             conn.ping(reconnect=True)
    #             sql = "SELECT * FROM basic_message WHERE id=" + ID + ";"
    #             cursor.execute(sql)
    #             conn.commit()
    #
    #             result = cursor.fetchall()
    #             result1 = list(result[4].values())
    #             # result1[2]=str(result1[2]).split('(')[0]
    #             return result1
    #         finally:
    #             conn.close()
    #
    #     # 查询博客
    # def search_bk(self):
    #         try:
    #             ID = self.id
    #             conn.ping(reconnect=True)
    #             sql = "SELECT * FROM basic_message WHERE id=" + ID + ";"
    #             cursor.execute(sql)
    #             conn.commit()
    #
    #             result = cursor.fetchall()
    #             result1 = list(result[5].values())
    #             # result1[2]=str(result1[2]).split('(')[0]
    #             return result1
    #         finally:
    #             conn.close()
    #
    # # 查询邮箱
    # def search_yx(self):
    #         try:
    #             ID = self.id
    #             conn.ping(reconnect=True)
    #             sql = "SELECT * FROM basic_message WHERE id=" + ID + ";"
    #             cursor.execute(sql)
    #             conn.commit()
    #
    #             result = cursor.fetchall()
    #             result1 = list(result[6].values())
    #             # result1[2]=str(result1[2]).split('(')[0]
    #             return result1
    #         finally:
    #             conn.close()
    #
    # # 查询简介
    # def search_jj(self):
    #         try:
    #             ID = self.id
    #             conn.ping(reconnect=True)
    #             sql = "SELECT * FROM basic_message WHERE id=" + ID + ";"
    #             cursor.execute(sql)
    #             conn.commit()
    #
    #             result = cursor.fetchall()
    #             result1 = list(result[7].values())
    #             # result1[2]=str(result1[2]).split('(')[0]
    #             return result1
    #         finally:
    #             conn.close()


    #修改用户密码
    def update_datas(self,ID,password):
        # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
        conn.ping(reconnect=True)
        # 插入sql语句
        sql = "UPDATE users SET password="+password+ " WHERE id=" + ID +";"
        # 执行sql语句
        cursor.execute(sql)
        conn.commit()
        conn.close()


    #销户
    def account_closure(ID):
        # ping()使用该方法 ping(reconnect=True)
        conn.ping(reconnect=True)
        sql = "DELETE FROM users WHERE id='" + ID + "' "
        cursor.execute(sql)
        # sql1="DELETE FROM users WHERE id='" + ID + "' "
        # cursor.execute(sql1)
        # sql2="DELETE FROM users WHERE id='" + ID + "' "
        # cursor.execute(sql2)
        # 提交到数据库执行
        conn.commit()
        # 关闭数据库
        conn.close()




    # #存款
    # def deposit(chun):
    #     # ping()使用该方法 ping(reconnect=True)
    #     ID=id
    #     conn.ping(reconnect=True)
    #     sql = "UPDATE users SET balance=balance+"+chun+" WHERE id="+ID
    #     cursor.execute(sql)
    #     sql2="INSERT INTO tradeInfo(tradeType,id,tradeMoney) VALUES('存入','"+ID+"','"+chun+"') "
    #     cursor.execute(sql2)
    #     # 提交到数据库执行
    #     conn.commit()
    #     # 关闭数据库
    #     conn.close()


    # #取款
    # def withdraw(qu):
    #    # ping()使用该方法 ping(reconnect=True)
    #    ID=id
    #    conn.ping(reconnect=True)
    #    sql = "UPDATE users SET balance=balance-"+qu+" WHERE id="+ID
    #    cursor.execute(sql)
    #
    #    sql2="INSERT INTO tradeInfo(tradeType,id,tradeMoney) VALUES('支出','"+ID+"','"+qu+"') "
    #    cursor.execute(sql2)
    #    # 提交到数据库执行
    #    conn.commit()
    #    # 关闭数据库
    #    conn.close()

    # #查询交易记录
    # def search_recording():
    #     # ping()使用该方法 ping(reconnect=True) ，那么可以在每次连接之前，会检查当前连接是否已关闭，如果连接关闭则会重新进行连接。
    #     conn.ping(reconnect=True)
    #     # 插入sql语句
    #     ID=id
    #     sql="SELECT * FROM tradeInfo WHERE id="+ID+";"
    #     # 执行sql语句
    #     cursor.execute(sql)
    #     results = cursor.fetchall()
    #     results1 = []
    #     for i in results:
    #         a=list(i.values())
    #         a[0]=str(a[0]).split('(')[0]
    #         results1.append(a)
    #     # 关闭数据库a
    #     conn.close()
    #     # 返回结果
    #     return results1
    
    # #转账
    # def transfer(mane,zrID):
    #     # ping()使用该方法 ping(reconnect=True)
    #     ID=id
    #     conn.ping(reconnect=True)
    #     sql = "UPDATE users SET balance=balance-"+mane+" WHERE id="+ID
    #     cursor.execute(sql)
    #     sql2="INSERT INTO tradeInfo(tradeType,id,tradeMoney) VALUES('支出','"+ID+"','"+mane+"') "
    #     cursor.execute(sql2)
    #     sql3="UPDATE users SET balance=balance+"+mane+" WHERE id="+zrID
    #     cursor.execute(sql3)
    #     sql4="INSERT INTO tradeInfo(tradeType,id,tradeMoney) VALUES('存入','"+zrID+"','"+mane+"') "
    #     cursor.execute(sql4)
    #     # 提交到数据库执行
    #     conn.commit()
    #     # 关闭数据库
    #     conn.close()


    # #查询类型
    # def search_type():
    #     ID=id
    #     conn.ping(reconnect=True)
    #     sql="SELECT type FROM deposit WHERE id="+ID+";"
    #     cursor.execute(sql)
    #     results = cursor.fetchone()
    #     return results

    # #挂失
    # def loss():
    #     ID=id
    #     conn.ping(reconnect=True)
    #     sql="UPDATE users SET isReportLoss='1' WHERE id="+ID+";"
    #     cursor.execute(sql)
    #     # 提交到数据库执行
    #     conn.commit()
    #     # 关闭数据库
    #     conn.close()

    # #解挂
    # def un_loss():
    #     ID=id
    #     conn.ping(reconnect=True)
    #     sql="UPDATE users SET isReportLoss='0' WHERE id="+ID+";"
    #     cursor.execute(sql)
    #     # 提交到数据库执行
    #     conn.commit()
    #     # 关闭数据库
    #     conn.close()
        

    

    