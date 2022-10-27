# 1、定义一个列表，将来用于存储所有学员的通讯信息
students = []

# 2、打印功能菜单
print('-' * 40)
print('欢迎使用传智教育通讯录管理系统V1.0')
print('[1] 增加学员信息')
print('[2] 删除学员信息')
print('[3] 退出系统')
print('-' * 40)

while True:
    # 3、提示用户进行相关操作
    user_num = int(input('请输入您要进行的操作编号：'))

    if user_num == 1:
        # 4、提示用户输入学员的信息
        student = {}
        student['name'] = input('请输入学员的姓名：')
        student['age'] = int(input('请输入学员的年龄：'))
        student['mobile'] = input('请输入学员的电话：')
        # 5、把学员信息保存在列表中
        students.append(student)
        print(students)

    elif user_num == 2:
        name = input('请输入要删除的学员信息：')
        # 6、遍历所有学员信息
        for i in students:
            if i['name'] == name:
                # 从列表中删除整个学员（字典）
                students.remove(i)
                print('删除成功')
                print(students)
            else:
                print('您要删除的学员信息不存在')

    elif user_num == 3:
        print('感谢您使用传智教育通讯录管理系统V1.0')
        break

    else:
        print('输入错误，请重新输入要操作的编号')
