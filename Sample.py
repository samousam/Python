# 导入驱动
import sqlite3
# 连接sqlite3数据库，数据库文件emp.db，如不存在，自动创建
connect = sqlite3.connect('sample.db')

# 创建cursor游标
cursor = connect.cursor()
# 如果没有创建表，执行sql语句，创建表
sql = '''create table if not exists emp (
      'id' int primary key, 
      'name' varchar(20), 
      'gender' varchar(20),
      'age' varchar(20))'''
# 执行sql创建表语句
cursor.execute(sql)
# 提交事务
connect.commit()

def menu():
    # 选择功能菜单
    print("-" * 10 + "员工管理系统" + "-" * 10)
    print("*"*30)
    print("1.添加员工信息")
    print("2.删除员工信息")
    print("3.修改员工信息")
    print("4.查看单个员工信息")
    print("5.查看所有员工信息")
    print("6.退出")
    print("*"*30)

# 增加
def addEmp():
    id = input("请输入要添加的员工编号：")
    while True:
        if checkID(id):
            print("已有此ID")
            id = input("请重新输入要添加的员工编号：")
        else:
            break
    name = input("请输入要添加的员工姓名：")
    gender = input("请输入要添加的员工性别：")
    age = input("请输入要添加的员工年龄：")

    cursor.execute(
        'INSERT INTO emp VALUES (?, ?, ?, ?)', (id, name, gender, age))
    # 要进行数据提交, 这样数据才会保存
    connect.commit()

    print("添加成功")

# 删除
def deleteEmp():
    id = input("请输入要删除的员工编号：")

    if not checkID(id):
        print("需要删除的员工编号不存在！")
        return

    cursor.execute(
            'DELETE FROM emp WHERE id=?', (id,))
    # 要进行数据提交这样数据才会保存
    connect.commit()
    print("删除成功")

# 修改
def updateEmp():
    id = input("请输入要修改的员工编号：")

    if not checkID(id):
        print("需要修改的员工编号不存在！")
        return

    name = input("请输入要修改后的员工姓名：")
    gender = input("请输入要修改后的员工性别：")
    age = input("请输入要修改后的员工年龄：")

    cursor.execute(
            'UPDATE emp SET gender=?,name=?,age=? WHERE id=?', (name, gender, age, id))
    # 对数据进行修改, 要提交事务, 这样修改才会保存
    connect.commit()
    print("修改成功！！！")

# 查制定id
def getEmpById():
    id = input("请输入要查询的员工编号：")
    cursor.execute(
        'SELECT * FROM emp where id=?', (id,))
    emps = cursor.fetchall()
    for emp in emps:
        print('查询结果如下:')
        print("编号 \t姓名 \t性别 \t年龄")
        print("{:^}\t\t{:^}\t\t{:^}\t\t{:^}".format(emp[0], emp[1], emp[2], emp[3]))
        break
    else:
        print("查无此人！！！")

# 查询所有
def getAllEmp():
    cursor.execute('SELECT * FROM emp')
    emps = cursor.fetchall()
    print('查询结果如下:')
    print("编号\t\t姓名\t\t性别\t\t年龄")
    for emp in emps:
        print("{:^}\t\t{:^}\t\t{:^}\t\t{:^}".format(emp[0], emp[1], emp[2], emp[3]))

# 判断id是否存在
def checkID (id):
    cursor.execute(
        'SELECT * FROM emp WHERE id=?', (id,))
    result = cursor.fetchone()
    return True if result else False

# if __name__ == '__main__':
while True:
    menu()
    choice = input("请输入您的选择：")
    if choice == '1':
        addEmp()
    elif choice == '2':
        deleteEmp()
    elif choice == '3':
        updateEmp()
    elif choice == '4':
        getEmpById()
    elif choice == '5':
        getAllEmp()
    elif choice == '6':
        # 关闭游标和数据库
        cursor.close()
        connect.close()
        print("退出成功！")
        break
    else:
        print("请输入正确的指令！")
