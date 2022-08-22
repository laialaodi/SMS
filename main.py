#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib.sql

user_password = {}

user_name = str()

link = None


def import_password() -> None:
    """由文件导入密码

    参数
        无

    返回值
        无
    """
    try:
        with open('password.txt', 'r') as f:
            lines = f.readlines()
        for line in lines:
            user_password[line.split()[0]] = line.split()[1]
    except:
        pass


def login():
    """登录系统

    参数
        无

    返回值
        无
    """
    global user_name
    print('欢迎进入系统')
    print('请登录')
    while 1:
        user_input = input('请输入用户名和密码:').strip().split()
        if user_input[0] not in user_password:
            print('账户注册须得到管理员的许可，请向管理员提出申请，让管理员为你创建一个账户')
        elif len(user_input) == 1:
            print('缺少用户名或密码!')
        elif user_password[user_input[0]] == user_input[1]:
            user_name = user_input[0]
            break
        else:
            print('用户名或密码错误!')


def import_data():
    """从文件导入json数据
    
    参数
        无

    返回值
        无
    """
    global link
    while 1:
        user_input = input('请输入导入文件名(初次使用请回车跳过):')
        if user_input == '':
            user_input = input('文件未创建，请设定初始的年级数和班级数:').strip().split()
            link = lib.sql.School(grades=int(
                user_input[0]), classes=int(user_input[1]))
            break
        else:
            link = lib.sql.School(grades=-1, classes=-1)
            return_status_code = link.from_file_load_student(user_input)
            if return_status_code == 0:
                print('导入成功')
                break
            elif return_status_code == -1:
                print('文件不存在!')


if __name__ == '__main__':
    import_password()

    login()

    import_data()

    print(f'欢迎您，{user_name}')
    print('添加学生: 1')
    print('删除学生: 2')
    print('查询学生: 3')
    print('退出系统: exit(直接退出不会保存!)')
    print('保存数据: save')
    print('导入(还原)数据: load')
    print('再次查看本帮助: help')
    while 1:
        user_input = input('请输入:')
        if user_input == 'exit':
            break
        elif user_input == 'save':
            save_file_name = input('请输入保存文件名:')
            return_status_code = link.save_student_to_file(save_file_name)
            if return_status_code == 0:
                pass
            elif return_status_code == -1:
                print('保存失败')
        elif user_input == 'load':
            load_file_name = input('请输入导入文件名:')
            return_status_code = link.from_file_load_student(load_file_name)
            if return_status_code == 0:
                pass
            elif return_status_code == -1:
                print('找不到文件')
        elif user_input == 'help':
            print('命令手册')
            print('添加学生: 1')
            print('删除学生: 2')
            print('查询学生: 3')
            print('退出系统: exit(直接退出不会保存!)')
            print('保存数据: save')
            print('导入(还原)数据: load')
        elif user_input == '1':
            print('例子:六年级是6，六(3)班级则是63')
            print('hint: 六(10)班仍然是610')
            user_input = input('请输入学生的年级班级姓名并用一个空格分开:').strip().split()
            grade = int(user_input[0])
            class_ = user_input[1]
            name = user_input[2]
            link.add_student(_grade=grade, _class=class_, _name=name)
        elif user_input == '2':
            print('例子:六年级是6，六(3)班级则是6 3')
            print('hint: 六(10)班仍然是6 10')
            user_input = input('请输入学生的年级班级姓名并用一个空格分开:').strip().split()
            grade = int(user_input[0])
            class_ = user_input[1]
            name = user_input[2]
            return_status_code = link.remove_student(
                _grade=grade, _class=class_, _name=name)
            if return_status_code == 0:
                pass
            elif return_status_code == -1:
                print('您删除了一个不存在的数值！')
        elif user_input == '3':
            print('例子:六年级是6，六(3)班级则是6 3')
            print('hint: 六(10)班仍然是6 10')
            user_input = input('请输入年级和班级:').strip()
            print(f'{user_input[0]}({user_input[1]})班的学生有:')
            # 这里user_input是列表，其中的每一项都是字符串
            link.list_student(*list(map(int, user_input.strip().split())))
        else:
            print('输入错误!')
    if save_file_name in locals():
        link.save_student_to_file(save_file_name)
        print('数据已保存')
    else:
        save_file_name = input('请输入保存文件名:')
        return_status_code = link.save_student_to_file(save_file_name)
        if return_status_code == 0:
            print('数据已保存')
        elif return_status_code == -1:
            print('保存失败')
